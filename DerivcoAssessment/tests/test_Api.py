import pytest
import jsonschema
from tests.conftest import search_cocktail_by_name_expected_response_schema
from utilities.base_class import BaseClass


class TestApi(BaseClass):
    # Test case for searching ingredients by name, see fixture for input parameters
    @pytest.mark.parametrize("ingredient_name, expected_alcohol_status", [
        ("vodka", "Yes"),  # Valid alcoholic ingredient
        ("orange juice", "No"),  # Valid non-alcoholic ingredient
        ("nonexistent", None),  # Non-existent ingredient
    ])
    def test_search_ingredients_by_name(self, ingredient_name, expected_alcohol_status):
        """
                Test searching ingredients by name.

                Args:
                    ingredient_name (str): The name of the ingredient to search for.
                    expected_alcohol_status (str): The expected alcohol status (Yes, No, or None).
                """

        ingredients = self.api_search_ingredient_by_name(ingredient_name)

        # Assertions: Check if ingredients is not null and access key values for validation
        if ingredients is not None:
            ingredient = ingredients.get("ingredients", [])
            if ingredient:
                assert ingredient[0]["strIngredient"].lower() == ingredient_name.lower()
                print(ingredient[0]["strIngredient"])
                assert ingredient[0]["strAlcohol"] == expected_alcohol_status
                print(ingredient[0]["strAlcohol"])
                # where drink is alcoholic, strAlcohol is 'yes' and strABV is not null
                assert ingredient[0]["strABV"] is not None if expected_alcohol_status == "Yes" else True
                print(ingredient[0]["strABV"])
            else:
                # where ingredient is null
                assert expected_alcohol_status is None
                print(f"None found for '{ingredient_name}'")

    ####################################################################################################################
    # Test case for searching cocktails by name, see fixture for input parameters
    @pytest.mark.parametrize("cocktail_name, expected_result", [
        ("Margarita", True),  # Valid cocktail
        ("Daiquiri", True),  # Valid cocktail
        ("Nonexistent", False),  # Non-existent cocktail
    ])
    def test_search_cocktails_by_name(self, cocktail_name, expected_result):
        """
            Test searching for cocktails by name using the API.

            Args:
                cocktail_name (str): The name of the cocktail to search for.
                expected_result (bool): The expected result, True if the cocktail is expected to be found, False otherwise.
            """

        data = self.api_search_cocktail_by_name(cocktail_name)

        # if cocktail not in db, returns as null and else block executed
        if data['drinks'] is not None:
            if "drinks" in data and data["drinks"]:
                self.api_format_search_cocktail_by_name_response(data["drinks"])
                # Assertions for valid cocktails
                assert data["drinks"] is not None and len(data["drinks"]) > 0
                cocktail = data["drinks"][0]
                assert cocktail["strDrink"].lower() == cocktail_name.lower()
                assert cocktail["strInstructions"] is not None

                # Schema validation - schema declared in conftest.py
                try:
                    jsonschema.validate(data, search_cocktail_by_name_expected_response_schema)
                    print("Schema validation passed")
                except jsonschema.ValidationError as e:
                    assert False, f"API response does not match expected schema: {e}"
            else:
                assert not expected_result
                print(f"No matching cocktails found for '{cocktail_name}'")
        else:
            assert data['drinks'] is None
            print(f"There are no drinks found for {cocktail_name}")
            assert not expected_result, f"No API response for {cocktail_name}"

    ####################################################################################################################
    # Additional test case: this test performs api calls on method List all cocktails by first letter
    # test runs 6 times with different first letter inputs (3 of which returns null value for 'drinks')
    # if input is valid, cocktail names found for the input is printed else program checks that value of drinks is null
    @pytest.mark.parametrize("first_letter", [
        " ",  # drinks will return as null with blank space
        "$",  # drinks will return as null with special character
        "u",  # drinks will return as null, no drinks start with 'u'
        "v",
        "w",
        1,
    ])
    def test_list_cocktails_by_first_letter(self, first_letter):
        """
                Test listing cocktails by the first letter of their name.

                Args:
                    first_letter (str): The first letter to filter cocktails by.
                """
        data = self.api_get_list_of_cocktails_by_first_letter(first_letter)

        if not data["drinks"]:  # when drinks is null execute this block
            assert data["drinks"] is None
            print(f"No drinks found for first letter '{first_letter}'")
        else:
            assert data["drinks"], f"Expected drinks for first_letter '{first_letter}' but found none"
            print(f"===Drinks found for first letter '{first_letter}'===\n")
            for i in range(len(data["drinks"])):
                drink_name = data["drinks"][i]["strDrink"]
                print(drink_name)

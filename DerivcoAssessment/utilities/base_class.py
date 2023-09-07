import json
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from tests.conftest import BASE_URI


@pytest.mark.usefixtures("setup")
class BaseClass:

    def api_search_ingredient_by_name(self, ingredient_name):
        """
                Search for an ingredient by name using the API.

                Args:
                    ingredient_name (str): The name of the ingredient to search for.

                Returns:
                    dict: The API response data as a dictionary.
                """

        response = self.api_session.get(BASE_URI + f"search.php?i={ingredient_name}")
        data = json.loads(response.text)
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        return data

    def api_search_cocktail_by_name(self, cocktail_name):
        """
               Search for a cocktail by name using the API.

               Args:
                   cocktail_name (str): The name of the cocktail to search for.

               Returns:
                   dict: The API response data as a dictionary.
               """
        response = self.api_session.get(BASE_URI + f"search.php?s={cocktail_name}")
        data = json.loads(response.text)
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        return data

    def api_format_search_cocktail_by_name_response(self, api_response):
        """
               Format and print the API response data for cocktails by name.

               Args:
                   api_response (list): The API response data as a list of cocktails.
               """
        for index, cocktail in enumerate(api_response):
            print(f"=== Cocktail {index + 1} ===")
            keys_to_extract = ["strDrink", "strTags", "strCategory", "strAlcoholic", "strGlass", "strInstructions",
                               "strIngredient1", "strMeasure1", "strCreativeCommonsConfirmed", "dateModified"]
            for key in keys_to_extract:
                value = cocktail.get(key, "Key not found")
                print(f"{key}: {value}")

    def api_search_cocktail_name_by_id(self, id):
        """
                Search for a cocktail by ID using the API.

                Args:
                    id (int): The ID of the cocktail to search for.

                Returns:
                    dict: The API response data as a dictionary.
                """
        response = self.api_session.get(BASE_URI + f"lookup.php?i={id}")
        data = json.loads(response.text)
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        return data

    def api_get_list_of_cocktails_by_first_letter(self, first_letter):
        """
                Get a list of cocktails starting with a specific letter using the API.

                Args:
                    first_letter (str): The first letter to filter cocktails by.

                Returns:
                    dict: The API response data as a dictionary.
                """
        response = self.api_session.get(BASE_URI + f"search.php?f={first_letter}")
        data = json.loads(response.text)
        assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}"
        return data

    def web_browse_cocktails_by_first_letter(self, first_letter):
        """
                Browse cocktails by first letter on a web page.

                Args:
                    first_letter (str): The first letter to search for on the web page.
                """
        try:
            letter_xpath = f"//a[normalize-space()='{first_letter}']"
            letter = self.driver.find_element(By.XPATH, letter_xpath)
            letter.click()
            # print(f"Browse cocktails with first letter {first_letter}")
        except NoSuchElementException as e:
            print(f"'{first_letter}' was not found", str(e))

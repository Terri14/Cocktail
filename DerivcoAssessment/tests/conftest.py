import pytest
import requests
from selenium import webdriver

BASE_URI = "https://www.thecocktaildb.com/api/json/v1/1/"

search_cocktail_by_name_expected_response_schema = {
    "type": "object",
    "properties": {
        "drinks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "strDrink": {"type": ["string", "null"]},
                    "strTags": {"type": ["string", "null"]},
                    "strCategory": {"type": ["string", "null"]},
                    "strAlcoholic": {"type": ["string", "null"]},
                    "strGlass": {"type": ["string", "null"]},
                    "strInstructions": {"type": ["string", "null"]},
                    "strInstructionsES": {"type": ["string", "null"]},
                    "strInstructionsDE": {"type": ["string", "null"]},
                    "strInstructionsFR": {"type": ["string", "null"]},
                    "strInstructionsIT": {"type": ["string", "null"]},
                    "strInstructionsZH-HANS": {"type": ["string", "null"]},
                    "strInstructionsZH-HANT": {"type": ["string", "null"]},
                    "strDrinkThumb": {"type": ["string", "null"]},
                    "strIngredient1": {"type": ["string", "null"]},
                    "strIngredient2": {"type": ["string", "null"]},
                    "strIngredient3": {"type": ["string", "null"]},
                    "strIngredient4": {"type": ["string", "null"]},
                    "strIngredient5": {"type": ["string", "null"]},
                    "strIngredient6": {"type": ["string", "null"]},
                    "strIngredient7": {"type": ["string", "null"]},
                    "strIngredient8": {"type": ["string", "null"]},
                    "strIngredient9": {"type": ["string", "null"]},
                    "strIngredient10": {"type": ["string", "null"]},
                    "strIngredient11": {"type": ["string", "null"]},
                    "strIngredient12": {"type": ["string", "null"]},
                    "strIngredient13": {"type": ["string", "null"]},
                    "strIngredient14": {"type": ["string", "null"]},
                    "strIngredient15": {"type": ["string", "null"]},
                    "strMeasure1": {"type": ["string", "null"]},
                    "strMeasure2": {"type": ["string", "null"]},
                    "strMeasure3": {"type": ["string", "null"]},
                    "strMeasure4": {"type": ["string", "null"]},
                    "strMeasure5": {"type": ["string", "null"]},
                    "strMeasure6": {"type": ["string", "null"]},
                    "strMeasure7": {"type": ["string", "null"]},
                    "strMeasure8": {"type": ["string", "null"]},
                    "strMeasure9": {"type": ["string", "null"]},
                    "strMeasure10": {"type": ["string", "null"]},
                    "strMeasure11": {"type": ["string", "null"]},
                    "strMeasure12": {"type": ["string", "null"]},
                    "strMeasure13": {"type": ["string", "null"]},
                    "strMeasure14": {"type": ["string", "null"]},
                    "strMeasure15": {"type": ["string", "null"]},
                    "strImageSource": {"type": ["string", "null"]},
                    "strImageAttribution": {"type": ["string", "null"]},
                    "strCreativeCommonsConfirmed": {"type": ["string", "null"]},
                    "dateModified": {"type": ["string", "null"]}
                },
                "required": [
                    "strDrink",
                    "strTags",
                    "strCategory",
                    "strAlcoholic",
                    "strGlass",
                    "strInstructions",
                    "strIngredient1",
                    "strMeasure1",
                    "strCreativeCommonsConfirmed",
                    "dateModified"
                ],
            }
        },
    },
    "required": ["drinks"],
}


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()


@pytest.fixture(scope="function")
def setup(request, api_session):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = None
    if "web" in request.keywords:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        url = "https://www.thecocktaildb.com/"
        driver.get(url)
        driver.maximize_window()
    request.cls.driver = driver
    request.cls.api_session = api_session

    yield driver

    if request.cls.driver:
        driver.close()

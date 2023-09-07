from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.base_class import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    browse_name_by_letter_bar = (By.XPATH, "//div[@class='row']//h2//a")
    cocktail_cards = (By.XPATH, "//div[@class='col-sm-3']")

    def get_list_of_letters(self):
        """
                Get a list of letters displayed on the homepage.

                Returns:
                    list: A list of letters.
                """
        first_letter_list_raw = self.driver.find_elements(*HomePage.browse_name_by_letter_bar)
        first_letter_list = []
        for letter in first_letter_list_raw:
            letter_text = letter.text
            first_letter_list.append(letter_text)
        return first_letter_list

    def get_names_of_cocktails_displayed_on_page(self):
        """
                Get the names of cocktails displayed on the homepage.

                Returns:
                    list: A list of cocktail names.
                """
        cocktails_raw_list = self.driver.find_elements(*HomePage.cocktail_cards)
        cocktails_list = []

        # exclude last two entries which appear in footer and not applicable
        cocktails_to_process = cocktails_raw_list[:-2]
        for cocktail_element in cocktails_to_process:
            cocktail_name = cocktail_element.text
            cocktails_list.append(cocktail_name)
        # print(f"Total cocktails on page for this letter : {len(cocktails_list)}")
        return cocktails_list

    def get_all_cocktails(self):
        """
                Get all cocktails displayed on the homepage.

                Returns:
                    list: A nested list of cocktail names grouped by letters.
                """
        first_letter_list = self.get_list_of_letters()
        all_cocktails_list = []
        for letter in first_letter_list:
            self.web_browse_cocktails_by_first_letter(letter)
            self.wait.until(EC.presence_of_all_elements_located(HomePage.cocktail_cards))
            cocktails_on_page = self.get_names_of_cocktails_displayed_on_page()
            all_cocktails_list.append(cocktails_on_page)
            self.driver.back()
            total_items = sum(len(sublist) for sublist in all_cocktails_list)
        print(f"Total items = {total_items}")
        return all_cocktails_list

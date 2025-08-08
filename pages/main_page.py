import time
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def accept_cookies(self):
        try:
            
            self.click(MainPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    def scroll_to_faq(self):
        self.scroll_to(MainPageLocators.FAQ_SECTION)

    def click_question(self, question_text):
        locator = MainPageLocators.FAQ_QUESTION(question_text)
        self.scroll_to(locator)
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_answer_snippet(self, expected_snippet):
        locator = MainPageLocators.FAQ_ANSWER(expected_snippet)
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)


    def click_order_button(self, index):
        buttons = self.driver.find_elements(*MainPageLocators.ORDER_BUTTONS)
        buttons[index].click()

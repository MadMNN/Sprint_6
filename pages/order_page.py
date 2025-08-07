from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.locators import MainPageLocators
from locators.locators import OrderLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def accept_cookies(self):
        try:
            
            self.click(MainPageLocators.COOKIE_BUTTON)
        except TimeoutException:
            pass

    def fill_personal_info(self, name, surname, address, metro, phone):
        self.driver.find_element(*OrderLocators.INPUT_NAME).send_keys(name)
        self.driver.find_element(*OrderLocators.INPUT_SURNAME).send_keys(surname)
        self.driver.find_element(*OrderLocators.INPUT_ADDRESS).send_keys(address)
        metro_input = self.driver.find_element(*OrderLocators.INPUT_METRO)
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.DOWN, Keys.ENTER)
        self.driver.find_element(*OrderLocators.INPUT_PHONE).send_keys(phone)
        self.driver.find_element(*OrderLocators.BUTTON_NEXT).click()

    def fill_order_details(self, date, rental_period, color, comment):
        self.driver.find_element(*OrderLocators.INPUT_DATE).send_keys(date, Keys.ENTER)
        self.driver.find_element(*OrderLocators.DROPDOWN_PERIOD).click()
        self.driver.find_element(*OrderLocators.DROPDOWN_OPTION(rental_period)).click()
        if color == 'black':
            self.driver.find_element(*OrderLocators.COLOR_BLACK).click()
        elif color == 'grey':
            self.driver.find_element(*OrderLocators.COLOR_GREY).click()
        self.driver.find_element(*OrderLocators.INPUT_COMMENT).send_keys(comment)
        self.driver.find_element(*OrderLocators.BUTTON_ORDER).click()

    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(OrderLocators.BUTTON_CONFIRM)).click()

    def get_order_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located(OrderLocators.MODAL_HEADER)).text

    def open_order_status(self):
        self.driver.find_element(*OrderLocators.BUTTON_STATUS).click()

  #  def is_cancel_button_present(self):
   #     return self.wait.until(EC.visibility_of_element_located(OrderLocators.BUTTON_CANCEL))

    def click_yandex_logo(self):
        self.driver.find_element(*OrderLocators.LOGO_YANDEX).click()

    def click_scooter_logo(self):
        self.driver.find_element(*OrderLocators.LOGO_SCOOTER).click()
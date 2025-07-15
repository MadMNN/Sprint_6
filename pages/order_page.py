from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(self, name, surname, address, metro, phone):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Имя']").send_keys(name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Фамилия']").send_keys(surname)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']").send_keys(address)
        metro_input = self.driver.find_element(By.CLASS_NAME, 'select-search__input')
        metro_input.send_keys(metro)
        metro_input.send_keys(Keys.DOWN, Keys.ENTER)
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(phone)
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()

    def fill_order_details(self, date, rental_period, color, comment):
        self.driver.find_element(By.XPATH, "//input[@placeholder='* Когда привезти самокат']").send_keys(date, Keys.ENTER)
        self.driver.find_element(By.CLASS_NAME, 'Dropdown-control').click()
        self.driver.find_element(By.XPATH, f"//div[text()='{rental_period}']").click()
        if color == 'black':
            self.driver.find_element(By.ID, 'black').click()
        elif color == 'grey':
            self.driver.find_element(By.ID, 'grey').click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Комментарий для курьера']").send_keys(comment)

        # нажимаем правильную кнопку "Заказать"
        self.driver.find_element(
        By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
        ).click()


    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Да']"))).click()

    def get_order_confirmation_text(self):
        return self.wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'
        ))).text

    def open_order_status(self):
        self.driver.find_element(By.XPATH, "//button[text()='Посмотреть статус']").click()

    def is_cancel_button_present(self):
        return self.wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME, 'Button_Button__ra12g.Button_Inverted__3IF-i'
        )))

    def click_yandex_logo(self):
        self.driver.find_element(By.CLASS_NAME, 'Header_LogoYandex__3TSOI').click()

    def click_scooter_logo(self):
        self.driver.find_element(By.CLASS_NAME, 'Header_LogoScooter__3lsAR').click()

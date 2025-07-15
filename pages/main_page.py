from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[text()='да все привыкли']"
            )))
            cookie_button.click()
        except:
            pass

    def scroll_to_faq(self):
        faq_section = self.driver.find_element(By.CLASS_NAME, 'accordion')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", faq_section)

    def click_question(self, question_text):
        question = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//div[@class='accordion__button' and text()='{question_text}']"
            ))
        )
        question.click()

    def get_answer_text(self, question_index):
        answer = self.wait.until(
            EC.visibility_of_element_located((
                By.ID, f"accordion__panel-{question_index}"
            ))
        )
        return answer.text

    def click_order_button(self, index=0):
        buttons = self.driver.find_elements(By.XPATH, "//button[text()='Заказать']")
        buttons[index].click()

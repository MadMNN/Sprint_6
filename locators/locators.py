from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_SECTION = (By.CLASS_NAME, "accordion")
    FAQ_QUESTION = lambda text: (By.XPATH, f"//div[contains(@class, 'accordion__button') and contains(text(), \"{text}\")]")
    FAQ_ANSWER = lambda text: (By.XPATH, f"//p[contains(text(), '{text}')]")
    ORDER_BUTTONS = (By.CLASS_NAME, "Button_Button__ra12g")

    
class OrderLocators:
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CLASS_NAME, "select-search__input")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    DROPDOWN_OPTION = staticmethod(lambda period: (By.XPATH, f"//div[text()='{period}']"))
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

#BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")

    BUTTON_CONFIRM = (By.XPATH, "//button[text()='Да']")
    MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    BUTTON_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']")
    BUTTON_CANCEL = (By.CLASS_NAME, "Button_Button__ra12g.Button_Inverted__3IF-i")

    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers.urls import MAIN_PAGE_URL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data.order_data import order_data



@pytest.mark.parametrize("data", order_data)
def test_successful_order(driver, data):
    main = MainPage(driver)
    order = OrderPage(driver)

    main.open(MAIN_PAGE_URL)
    main.accept_cookies()
    main.click_order_button(data["entry_button_index"])

    order.fill_personal_info(data["name"], data["surname"], data["address"], data["metro"], data["phone"])
    order.fill_order_details(data["date"], data["rental_period"], data["color"], data["comment"])
    order.confirm_order()

    confirmation_text = order.get_order_confirmation_text()
    assert "Заказ оформлен" in confirmation_text

   # order.open_order_status()
   # assert order.is_cancel_button_present()

def test_redirect_yandex(driver):
    main = MainPage(driver)
    order = OrderPage(driver)

    main.open(MAIN_PAGE_URL)
    main.accept_cookies()

    original_window = driver.current_window_handle
    order.click_yandex_logo()

    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    new_window = [w for w in driver.window_handles if w != original_window][0]
    driver.switch_to.window(new_window)

    # Ждём, пока в текущем URL появится dzen.ru (неважно, через редирект или нет)
    WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
    assert "dzen.ru" in driver.current_url

    driver.close()
    driver.switch_to.window(original_window)


def test_redirect_scooter(driver):
    main = MainPage(driver)
    main.open(MAIN_PAGE_URL)
    main.accept_cookies()

    order = OrderPage(driver)
    order.click_scooter_logo()

    assert MAIN_PAGE_URL in driver.current_url

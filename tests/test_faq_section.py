import pytest
from pages.main_page import MainPage
from helpers.urls import MAIN_PAGE_URL

faq_data = [
    (0, 'Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей'),
    (1, 'Хочу сразу несколько самокатов! Так можно?', 'один заказ — один самокат'),
    (2, 'Как рассчитывается время аренды?', 'Отсчёт времени аренды'),
    (3, 'Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня'),
    (4, 'Можно ли продлить заказ или вернуть самокат раньше?', 'всегда можно позвонить'),
    (5, 'Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой'),
    (6, 'Можно ли отменить заказ?', 'Штрафа не будет'),
    (7, 'Я жизу за МКАДом, привезёте?', 'Всем самокатов')
]

@pytest.mark.parametrize('index, question_text, expected_snippet', faq_data)
def test_faq_answer_display(driver, index, question_text, expected_snippet):
    page = MainPage(driver)
    page.open(MAIN_PAGE_URL)
    page.accept_cookies()
    page.scroll_to_faq()
    page.click_question(question_text)
    answer = page.get_answer_text(index)
    assert expected_snippet in answer

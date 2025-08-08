import pytest
from pages.main_page import MainPage
from helpers.urls import MAIN_PAGE_URL

from data.faq_data import faq_data



@pytest.mark.parametrize('index, question_text, expected_snippet', faq_data)
def test_faq_answer_display(driver, index, question_text, expected_snippet):
    page = MainPage(driver)
    page.open(MAIN_PAGE_URL)
    page.accept_cookies()
    page.scroll_to_faq()
    page.click_question(question_text)
    answer = page.get_answer_snippet(expected_snippet)
    assert expected_snippet in answer

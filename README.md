# Sprint_6: UI-тесты для сервиса Яндекс.Самокат

Этот проект создан для автоматизации UI-тестирования учебного сервиса **Яндекс.Самокат**.

## 📌 Технологии
- Python
- Selenium
- Pytest
- Allure

## 📁 Структура проекта

```
Sprint_6/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── helpers/
│   └── urls.py
├── pages/
│   ├── main_page.py
│   └── order_page.py
└── tests/
    ├── test_faq_section.py
    └── test_order_scooter.py
```

## 🚀 Как запустить

1. Установи зависимости:
```bash
pip install -r requirements.txt
```

2. Установи GeckoDriver для Firefox.

3. Запусти тесты:
```bash
pytest
```

4. Посмотри отчёт Allure:
```bash
allure serve allure-results
```

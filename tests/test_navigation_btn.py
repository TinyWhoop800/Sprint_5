from pages.main_page import MainPage
from test_data import AUTH_VALID_EMAIL, AUTH_VALID_PASSWORD


class TestNavigationBtn:
    def test_navigation_to_constructor_on_click(self, driver):
        """Проверяет переход в конструктор при клике на кнопку "Конструктор" """
        page = MainPage(driver)
        page.open_login_page()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.click_personal_account_btn()
        page.click_constructor_btn()
        assert page.is_main_page()

    def test_navigation_to_homepage_on_logo_click(self, driver):
        """Проверяет переход на главную страницу при клике на логотип """
        page = MainPage(driver)
        page.open_login_page()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.click_personal_account_btn()
        page.click_logo_btn()
        assert page.is_main_page()
from pages.main_page import MainPage
from test_data import AUTH_VALID_EMAIL, AUTH_VALID_PASSWORD


class TestLogout:
    def test_logout_via_account_logout_button(self, driver):
        """Проверяет выход из аккаунта через кнопку "Выход" """
        page = MainPage(driver)
        page.open_login_page()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.click_personal_account_btn()
        page.assert_present_logout_btn()
        page.click_logout_btn()
        page.check_login_page()
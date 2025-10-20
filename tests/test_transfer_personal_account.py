from pages.main_page import MainPage
from test_data import AUTH_VALID_EMAIL, AUTH_VALID_PASSWORD


class TestTransferPersonalAccount:
    def test_valid_password(self, driver):
        """Проверяет вход и переход в личный кабинет """
        page = MainPage(driver)
        page.open_login_page()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.click_personal_account_btn()
        page.assert_elements_present_in_personal_account_page()
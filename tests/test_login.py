from pages.main_page import MainPage
from test_data import AUTH_VALID_PASSWORD, AUTH_VALID_EMAIL


class TestLoginPage:
    def test_login_via_main_page_login_button(self, driver):
        """Вход в аккаунт по кнопке "Войти в аккаунт" на главной """
        page = MainPage(driver)
        page.open_main_page()
        page.click_login_account_btn()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.check_main_page()

    def test_login_via_personal_account_button(self, driver):
        """Вход в аккаунт по кнопке "Личный кабинет" на странице "Главная" """
        page = MainPage(driver)
        page.open_main_page()
        page.click_personal_account_btn()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.check_main_page()

    def test_login_via_registration_page(self, driver):
        """Вход по кнопке "Войти" на странице "Регистрация" """
        page = MainPage(driver)
        page.open_registration_page()
        page.reg_click_login_btn()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.check_main_page()

    def test_login_via_password_recovery_form_login_button(self, driver):
        """Вход через страницу "Восстановление пароля" """
        page = MainPage(driver)
        page.open_password_recovery_page()
        page.recovery_password_click_login_btn()
        page.log_input_text_email(AUTH_VALID_EMAIL)
        page.log_input_text_password(AUTH_VALID_PASSWORD)
        page.click_log_in_btn()
        page.check_main_page()
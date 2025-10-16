from pages.main_page import MainPage
import pytest
from test_data import generate_email, generate_password, AUTH_VALID_NAME

name = AUTH_VALID_NAME
password = generate_password()


class TestRegistrationPage:
    @pytest.mark.parametrize('valid_password', ['qwerty', 'a' * 50])
    def test_valid_password(self, driver, valid_password):
        """Проверка регистрации, при вводе валидного пароля "6 символов" и "50 символов" """
        page = MainPage(driver)
        page.open_registration_page()
        page.reg_input_text_name(name)
        page.reg_input_text_email(generate_email())
        page.reg_input_text_password(valid_password)
        page.click_reg_account_btn()
        page.assert_elements_present_in_login_page()

    @pytest.mark.parametrize('invalid_password', ['q', 'qwert'])
    def test_invalid_password(self, driver, invalid_password):
        """Проверка регистрации, при вводе невалидного пароля "1 символ" и "5 символов" """
        page = MainPage(driver)
        page.open_registration_page()
        page.reg_input_text_name(name)
        page.reg_input_text_email(generate_email())
        page.reg_input_text_password(invalid_password)
        page.click_reg_account_btn()
        page.assert_elements_present_error_password_msg()
from pages.base_page import BasePage
from locators.main_locators import MainLocators
from test_data import MAIN_URL, REGISTRATION_URL, PASSWORD_RECOVERY_URL, LOGIN_URL

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = MainLocators
        self.MAIN_URL = MAIN_URL
        self.REGISTRATION_URL = REGISTRATION_URL
        self.PASSWORD_RECOVERY_URL = PASSWORD_RECOVERY_URL
        self.LOGIN_URL = LOGIN_URL

    # Локаторы на странице "Войти"
    ELEMENTS_LOGIN_PAGE = [
        MainLocators.LOG_EMAIL_INPUT,
        MainLocators.LOG_PASSWORD_INPUT,
        MainLocators.LOG_LOGIN_BUTTON,
        MainLocators.LOG_REGISTER_LINK
    ]

    # Локаторы на странице "Личный кабинет"
    ELEMENTS_PERSONAL_ACCOUNT_PAGE = [
        MainLocators.PA_PROFILE_BTN,
        MainLocators.PA_ORDER_HISTORY_BTN,
        MainLocators.PA_EXIT_BTN,
        MainLocators.PA_CANCEL_BTN,
        MainLocators.PA_SAVE_BTN
    ]

    # Открытие страниц
    def open_main_page(self):
        """ Открыть страницу "Главная" """
        self.open(self.MAIN_URL)

    def open_registration_page(self):
        """Открыть страницу "Регистрация" """
        self.open(self.REGISTRATION_URL)

    def open_password_recovery_page(self):
        """Открыть страницу "Восстановить пароль" """
        self.open(self.PASSWORD_RECOVERY_URL)

    def open_login_page(self):
        """Открыть страницу "Вход" """
        self.open(self.LOGIN_URL)

    # Навигация
    def click_personal_account_btn(self):
        """Клик по кнопке "Личный аккаунт" """
        self.click(self.locator.NAV_PERSONAL_ACCOUNT_BTN)

    def click_constructor_btn(self):
        """Клик по кнопке "Конструктор" """
        self.click(self.locator.NAV_CONSTRUCTOR_BTN)

    def click_logo_btn(self):
        """Клик по Лого"""
        self.click(self.locator.NAV_LOGO_BTN)

    # Страница "Главная"
    def click_login_account_btn(self):
        """Клик по кнопке "Войти в аккаунт" """
        self.click(self.locator.MAIN_LOGIN_BTN)

    def check_main_page(self):
        """Проверяем, что мы на главной странице """
        self.wait_for_url(self.MAIN_URL)
        current_url = self.get_current_url()
        assert current_url == self.MAIN_URL, f'Ожидался {self.MAIN_URL}, получен: {current_url}'

    def click_buns_section(self):
        """Клик на раздел "Булки" в блоке "Соберите бургер" """
        self.click(self.locator.MAIN_BUNS_TAB)

    def is_buns_visible(self):
        """Проверяем, что эемент "Булки" в блоке "Соберите бургер" стал активным """
        return self.wait_for_visibility(self.locator.MAIN_BUNS_TAB_ACTIVE).is_displayed()

    def click_sauces_section(self):
        """Клик на раздел "Соусы" в блоке "Соберите бургер" """
        self.click(self.locator.MAIN_SAUCES_TAB)

    def is_sauces_visible(self):
        """Проверяем, что эемент "Соусы" в блоке "Соберите бургер" стал активным """
        return self.wait_for_visibility(self.locator.MAIN_SAUCES_TAB_ACTIVE).is_displayed()

    def click_fillings_section(self):
        """Клик на раздел "Начинки" в блоке "Соберите бургер" """
        self.click(self.locator.MAIN_FILLINGS_TAB)

    def is_fillings_visible(self):
        """Проверяем, что эемент "Начинки" в блоке "Соберите бургер" стал активным """
        return self.wait_for_visibility(self.locator.MAIN_FILLINGS_TAB_ACTIVE).is_displayed()

    # Страница "Вход"
    def log_input_text_email(self, email):
        """Ввод текста в поле "Email" """
        self.input_text(self.locator.LOG_EMAIL_INPUT, email)

    def log_input_text_password(self, password):
        """Ввод текста в поле "Password" """
        self.input_text(self.locator.LOG_PASSWORD_INPUT, password)

    def click_log_in_btn(self):
        """Клик кнопки "Войти" """
        self.click(self.locator.LOG_LOGIN_BUTTON)

    def click_register_btn(self):
        """Клик по кнопке "Регистрация" """
        self.click(self.locator.LOG_REGISTER_LINK)

    def assert_elements_present_in_login_page(self):
        """Поиск элементов на странице "Вход" """
        assert self.are_element_present(self.ELEMENTS_LOGIN_PAGE), 'Регистрация неуспешная, не все элементы были найдены'

    def check_login_page(self):
        """Проверяем, что мы на главной странице """
        self.wait_for_url(self.LOGIN_URL)
        current_url = self.get_current_url()
        assert current_url == self.LOGIN_URL, f'Ожидался {self.LOGIN_URL}, получен: {current_url}'

    # Страница "Регистрация"
    def reg_input_text_name(self, name):
        """Ввод текста в поле "Имя" """
        self.input_text(self.locator.REG_NAME_INPUT, name)

    def reg_input_text_email(self, email):
        """Ввод текста в поле "Email" """
        self.input_text(self.locator.REG_EMAIL_INPUT, email)

    def reg_input_text_password(self, password):
        """Ввод текста в поле "Пароль" """
        self.input_text(self.locator.REG_PASSWORD_INPUT, password)

    def click_reg_account_btn(self):
        """Тап по кнопке "Зарегистрироваться" """
        self.click(self.locator.REG_REGISTER_BUTTON)

    def assert_elements_present_error_password_msg(self):
        """Поиск элемента "Неккоректный пароль" при вводе неверного пароля """
        assert self.find(self.locator.LOG_PASSWORD_INPUT), 'Ошибки "Неккоректный пароль" нет'

    def reg_click_login_btn(self):
        """Клик по кнопке "Войти" """
        self.click(self.locator.REG_LOGIN_LINK_BTN)

    # Страница "Восстановить пароль"
    def recovery_password_click_login_btn(self):
        """Клик по кнопке "Войти" """
        self.click(self.locator.RESET_LOGIN_BTN)

    def assert_elements_present_in_personal_account_page(self):
        """Поиск элементов на странице "Вход" """
        assert self.are_element_present(self.ELEMENTS_PERSONAL_ACCOUNT_PAGE), 'Не найдены элементы на странице "Персональный аккаунт"'

    # Страница "Личный аккаунт"
    def assert_present_logout_btn(self):
        """Ищем кнопку "Выйти" """
        assert self.find(self.locator.PA_PROFILE_BTN), 'Кнопка "Выйти" не найдена'

    def click_logout_btn(self):
        """Тап по кнопке "Выйти" """
        self.click(self.locator.PA_EXIT_BTN)
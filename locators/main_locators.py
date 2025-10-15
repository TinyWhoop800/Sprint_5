from selenium.webdriver.common.by import By

class MainLocators:
    # Навигация
    NAV_PERSONAL_ACCOUNT_BTN = (By.CSS_SELECTOR, 'nav a[href="/account"]') # Кнопка "Личный кабинет"
    NAV_CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор"
    NAV_LOGO_BTN = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]") # Логотип

    # Главная страница
    MAIN_LOGIN_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка "Войти в аккаунт"
    MAIN_BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Булки']]") # Кнопка раздела "Булки"
    MAIN_SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Соусы']]") # Кнопка раздела "Соусы"
    MAIN_FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and span[text()='Начинки']]") # Кнопка раздела "Начинки"
    MAIN_BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Булки']]") # Активная кнопка раздела "Булки"
    MAIN_SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Соусы']]") # Активная кнопка раздела "Соусы"
    MAIN_FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc') and span[text()='Начинки']]") # Активная кнопка раздела "Начинки"

    # Страница Регистрации
    REG_NAME_INPUT = (By.XPATH, '//div[label[text()="Имя"]]//input') # Поле ввода "Имя"
    REG_EMAIL_INPUT = (By.XPATH, '//div[label[text()="Email"]]//input') # Поле ввода "Email"
    REG_PASSWORD_INPUT = (By.XPATH, '//div[label[text()="Пароль"]]//input') # Поле ввода "Пароль"
    REG_REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]') # Кнопка "Зарегистрироваться"
    REG_LOGIN_LINK_BTN = (By.XPATH, "//a[text()='Войти']") # Кнопка "Войти"

    # Страница Входа
    LOG_EMAIL_INPUT = (By.XPATH, '//div[label[text()="Email"]]//input') # Поле ввода "Email"
    LOG_PASSWORD_INPUT = (By.XPATH, '//div[label[text()="Пароль"]]//input') # Поле ввода "Пароль"
    LOG_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') # Кнопка "Войти"
    LOG_REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"
    LOG_ERROR_MSG_PASSWORD = (By.CSS_SELECTOR, '.input__error.text_type_main-default') # Ошибка при неверном вводе пароля

    # Страница Восстановления пароля
    RESET_LOGIN_BTN = (By.XPATH, "//a[text()='Войти']") # Кнопка "Войти"

    # Страница "Личный кабинет"
    PA_PROFILE_BTN = (By.XPATH, "//a[text()='Профиль']") # Кнопка "Профиль"
    PA_ORDER_HISTORY_BTN = (By.XPATH, "//a[text()='История заказов']") # Кнопка "История заказов"
    PA_EXIT_BTN = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход"
    PA_CANCEL_BTN = (By.XPATH, "//button[text()='Отмена']") # Кнопка "Отмена"
    PA_SAVE_BTN = (By.XPATH, "//button[text()='Сохранить']") # Кнопка "Сохранить"
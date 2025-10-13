from selenium.webdriver.common.by import By

class MainLocators:
    # Навигация
    NAV_PERSONAL_ACCOUNT_BTN = (By.CSS_SELECTOR, 'nav a[href="/account"]') # Кнопка "Личный кабинет"
    NAV_CONSTRUCTOR_BTN = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p') # Кнопка "Конструктор"
    NAV_LOGO_BTN = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') # Логотип

    # Главная страница
    MAIN_LOGIN_BTN = (By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg') # Кнопка "Войти в аккаунт"
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
    REG_LOGIN_LINK_BTN = (By.CLASS_NAME, 'Auth_link__1fOlj') # Кнопка "Войти"

    # Страница Входа
    LOG_EMAIL_INPUT = (By.XPATH, '//div[label[text()="Email"]]//input') # Поле ввода "Email"
    LOG_PASSWORD_INPUT = (By.XPATH, '//div[label[text()="Пароль"]]//input') # Поле ввода "Пароль"
    LOG_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]') # Кнопка "Войти"
    LOG_REGISTER_LINK = (By.XPATH, '//a[text()="Зарегистрироваться" and contains(@class, "Auth_link__1fOlj")]') # Кнопка "Зарегистрироваться"
    LOG_ERROR_MSG_PASSWORD = (By.CLASS_NAME, 'input__error text_type_main-default') # Ошибка при неверном вводе пароля

    # Страница Восстановления пароля
    RESET_LOGIN_BTN = (By.CLASS_NAME, 'Auth_link__1fOlj')  # Кнопка "Войти"

    # Страница "Личный кабинет"
    PA_PROFILE_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')  # Кнопка "Профиль"
    PA_ORDER_HISTORY_BTN = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a')  # Кнопка "История заказов"
    PA_EXIT_BTN = (By.CSS_SELECTOR, "button.Account_button__14Yp3.text.text_type_main-medium.text_color_inactive")  # Кнопка "Выход"
    PA_CANCEL_BTN = (By.CLASS_NAME, 'button_button__33qZ0.button_button_type_secondary__3-tsA.button_button_size_medium__3zxIa')  # Кнопка "Отмена"
    PA_SAVE_BTN = (By.CLASS_NAME, 'button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa')  # Кнопка "Сохранить"
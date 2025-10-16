import random
import string

AUTH_VALID_NAME = "Artem"
AUTH_VALID_EMAIL = "artem_galkin_33_100@ya.ru"
AUTH_VALID_PASSWORD = "qwe123"

# Страница "Главная"
MAIN_URL = "https://stellarburgers.education-services.ru/"
# Страница "Регистрация"
REGISTRATION_URL = "https://stellarburgers.education-services.ru/register"
# Страница "Восстановить пароль"
PASSWORD_RECOVERY_URL = "https://stellarburgers.education-services.ru/forgot-password"
# Страница "Вход"
LOGIN_URL = "https://stellarburgers.education-services.ru/login"

def generate_email():
    domains = ["yandex.ru", "gmail.com", "ya.ru"]
    name = "artem"
    surname = "galkin"
    cohort = "33"
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{name}_{surname}_{cohort}_{random_digits}@{random.choice(domains)}"
    return email

def generate_password(min_length=6, max_length=20):
    length = random.randint(min_length, max_length)
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
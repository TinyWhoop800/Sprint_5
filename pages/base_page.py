from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """Создает объект страницы"""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        """Нажать на элемент"""
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        """Ввести текст в поле"""
        self.driver.find_element(*locator).send_keys(text)

    def open(self, url):
        """Открыть страницу по URL"""
        self.driver.get(url)

    def find(self, locator, timeout=5):
        """Найти элемент с ожиданием. Возвращает элемент или None"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def are_element_present(self, locators_list):
        """Проверить наличие всех элементов из списка"""
        for locator in locators_list:
            if self.find(locator) is None:
                return False
        return True

    def is_current_url(self, expected_url, exact_match=True, timeout=5):
        """Проверить URL страницы."""
        try:
            wait = WebDriverWait(self.driver, timeout)
            if exact_match:
                condition = EC.url_to_be(expected_url)
            else:
                condition = EC.url_contains(expected_url)
            wait.until(condition)
            return True
        except TimeoutException:
            return False

    def wait_for_visibility(self, locator):
        """Ждать, пока элемент станет видимым. Возвращает элемент."""
        return self.wait.until(EC.visibility_of_element_located(locator))
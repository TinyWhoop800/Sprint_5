from pages.main_page import MainPage

class TestLogout:
    def test_navigation_to_buns_section(self, driver):
        """Проверяет переход и активность вкладки "Булки" """
        page = MainPage(driver)
        page.open_main_page()
        page.click_fillings_section()
        page.is_fillings_visible()
        page.click_buns_section()
        assert page.is_buns_visible(), 'Элемент "Булки" не стал активным'

    def test_navigation_to_sauces_section(self, driver):
        """Проверяет переход и активность вкладки "Соусы" """
        page = MainPage(driver)
        page.open_main_page()
        page.click_sauces_section()
        assert page.is_sauces_visible(), 'Элемент "Соусы" не стал активным'

    def test_navigation_to_fillings_section(self, driver):
        """Проверяет переход и активность вкладки "Начинки" """
        page = MainPage(driver)
        page.open_main_page()
        page.click_fillings_section()
        assert page.is_fillings_visible(), 'Элемент "Начинки" не стал активным'
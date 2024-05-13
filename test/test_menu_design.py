from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import StellarBurgersUrl as Url
from data import StellarBurgersLogin as Login
from locators import StellarBurgersLocators


class TestStellarBurgersMenuDesign:


    def test_menu_design_rolls(self, driver):
        driver.find_element(*StellarBurgersLocators.CURRENT_TAB)
        active_tab = driver.find_element(*StellarBurgersLocators.CURRENT_TAB).text
        assert active_tab == 'Булки'

    def test_menu_design_souce(self, driver):
        driver.find_element(*StellarBurgersLocators.SOUCE_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.CURRENT_TAB)
        active_tab = driver.find_element(*StellarBurgersLocators.CURRENT_TAB).text
        assert active_tab == 'Соусы'

    def test_menu_design_filling(self, driver):
         driver.find_element(*StellarBurgersLocators.FILLING_BUTTON).click()
         driver.find_element(*StellarBurgersLocators.CURRENT_TAB)
         active_tab = driver.find_element(*StellarBurgersLocators.CURRENT_TAB).text
         assert active_tab == 'Начинки'

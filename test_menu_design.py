from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from data import get_sign_up_data
from locators import StellarBurgersLocators

class TestStellarBurgersMenuDesign:

    def test_menu_design_rolls(self, driver):
        driver.find_element(*StellarBurgersLocators.SOUCE_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.ROLLS_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ROLLS_PICTURE))
        rolls_picture = driver.find_element(*StellarBurgersLocators.ROLLS_PICTURE)
        assert rolls_picture.is_displayed()

    def test_menu_design_souce(self, driver):
        driver.find_element(*StellarBurgersLocators.SOUCE_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SOUCE_PICTURE))
        souce_picture = driver.find_element(*StellarBurgersLocators.SOUCE_PICTURE)
        assert souce_picture.is_displayed()

    def test_menu_design_filling(self, driver):
        driver.find_element(*StellarBurgersLocators.FILLING_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.FILLING_PICTURE))
        filling_picture = driver.find_element(*StellarBurgersLocators.FILLING_PICTURE)
        assert filling_picture.is_displayed()

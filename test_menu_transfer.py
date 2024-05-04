from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from data import get_sign_up_data
from locators import StellarBurgersLocators

class TestStellarBurgersMenuTransfer:

    def test_menu_transfer_personal_account(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("pavel_pliasunov_8_888@yandex.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("12345678")
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert driver.current_url == f'{URL}account', "Url is wrong"

    def test_menu_transfer_personal_account_to_design(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("pavel_pliasunov_8_888@yandex.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("12345678")
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.DESIGNER_BUTTON).click()
        assert driver.current_url == f'{URL}', "Url is wrong"

    def test_menu_exit_from_account(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("pavel_pliasunov_8_888@yandex.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("12345678")
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.EXIT_BUTTON))
        driver.find_element(*StellarBurgersLocators.EXIT_BUTTON).click()
        assert driver.current_url == f'{URL}account/profile', "Url is wrong"

    def test_menu_transfer_logo(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("pavel_pliasunov_8_888@yandex.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("12345678")
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGO_BUTTON).click()
        rolls_picture = driver.find_element(*StellarBurgersLocators.ROLLS_PICTURE)
        assert rolls_picture.is_displayed()



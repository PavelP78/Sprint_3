from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import StellarBurgersUrl as Url
from data import StellarBurgersLogin as Login
from locators import StellarBurgersLocators
from helpers import get_sign_up_data

class TestStellarBurgersEnter:

    def test_main_enter(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(*Login.MY_LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(*Login.MY_PASSWORD)
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_personal_account_enter(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(*Login.MY_LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(*Login.MY_PASSWORD)
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_registration_form_enter(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_REGISTRATION_FORM).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(*Login.MY_LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(*Login.MY_PASSWORD)
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()

    def test_password_recovery_form_enter(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.BUTTON_PASSWORD_RECOVERY_FORM).click()
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_PASSWORD_RECOVERY_FORM).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(*Login.MY_LOGIN)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(*Login.MY_PASSWORD)
        driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
        order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
        assert order_button.is_displayed()



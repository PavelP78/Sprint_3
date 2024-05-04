from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from data import get_sign_up_data
from locators import StellarBurgersLocators


class TestStellarBurgersRegistration:


    def test_main_page(self, driver):
        assert driver.current_url == f'{URL}', "Url is wrong"

    def test_registration(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REGISTRATION).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_REGISTRATION).send_keys(password_data)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON_REGISTRATION).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON))
        personal_account_button = driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        assert personal_account_button.is_displayed()

    def test_signup_registration_error_password(self, driver):
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*StellarBurgersLocators.NAME_FIELD).send_keys(name_data)
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REGISTRATION).send_keys(email_data)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_REGISTRATION).send_keys("123")
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON_REGISTRATION).click()
        error_password_registration = driver.find_element(*StellarBurgersLocators.ERROR_PASSWORD_REGISTRATION)
        assert error_password_registration.is_displayed()



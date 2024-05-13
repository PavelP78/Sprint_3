from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import StellarBurgersUrl as Url
from data import StellarBurgersLogin as Login
from locators import StellarBurgersLocators
from helpers import get_sign_up_data


class TestStellarBurgersRegistration:


    def test_main_page(self, driver):
        driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
        main_page = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        assert main_page.is_displayed()
        assert driver.current_url == f'{Url.URL_LOGIN}', "Url is wrong"

    def test_registration(self, driver):
          driver.find_element(*StellarBurgersLocators.MAIN_ENTER_BUTTON).click()
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




import pytest
from selenium import webdriver
from config import StellarBurgersResolution as Resolution
from data import StellarBurgersUrl as Url

def browser_setting():
     chrome_option = webdriver.ChromeOptions()
     chrome_option.add_argument(f'--window size={Resolution.RESOLUTION[0]},{Resolution.RESOLUTION[1]}')
     return chrome_option

@pytest.fixture
def driver():
     chrome = webdriver.Chrome(options=browser_setting())
     chrome.get(Url.URL_MAIN)

     yield chrome

     chrome.quit()

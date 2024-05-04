import pytest
from selenium import webdriver
from config import URL,RESOLUTION

def browser_setting():
     chrome_option = webdriver.ChromeOptions()
     chrome_option.add_argument(f'--window size={RESOLUTION[0]}, {RESOLUTION[1]}')
     return chrome_option

@pytest.fixture
def driver():
     chrome = webdriver.Chrome(options=browser_setting())
     chrome.get(URL)

     yield chrome

     chrome.quit()

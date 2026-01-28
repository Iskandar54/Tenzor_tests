import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--headless")  
    options.add_argument("--disable-gpu") 
    options.add_argument("--window-size=1920,1080")  
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage") 

    driver = webdriver.Chrome(options=options)

    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
    "latitude": 54.7388,
    "longitude": 55.9721,
    "accuracy": 100
    })
    driver.execute_cdp_cmd(
        "Browser.grantPermissions",
        {"origin": "https://saby.ru", "permissions": ["geolocation"]}
    )

    yield driver

    driver.quit()

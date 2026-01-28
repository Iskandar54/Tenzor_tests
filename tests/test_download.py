import os
import time
from pages.saby_download_page import SabyDownloadPage
from utils.logger import logger

def test_download_saby(driver):

    page = SabyDownloadPage(driver)
    page.open()
    page.go_to_download_page()

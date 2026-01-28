from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SabyDownloadPage(BasePage):
    BASE_URL = "https://saby.ru"
    FOOTER_DOWNLOAD = (By.XPATH, "//a[contains(text(),'Скачать локальные версии')]")
    WINDOWS_DESKTOP = (By.XPATH, "//a[contains(@href,'exe')]")

    def open(self):
        self.driver.get(self.BASE_URL)

    def go_to_download_page(self):
        self.scroll_to_bottom()
        self.click(self.FOOTER_DOWNLOAD)

    def download_windows(self):
        self.click(self.WINDOWS_DESKTOP)

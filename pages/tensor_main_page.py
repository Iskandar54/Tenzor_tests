from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TensorMainPage(BasePage):

    PEOPLE_POWER_BLOCK = (By.XPATH, "//p[text()='Сила в людях']")

    MORE_DETAILS_BUTTON = (By.XPATH, "//a[contains(@href, '/about')]")

    def is_people_power_block_visible(self):
        return self.find(self.PEOPLE_POWER_BLOCK).is_displayed()

    def click_more_details(self):
        self.click(self.MORE_DETAILS_BUTTON)

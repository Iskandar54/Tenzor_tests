from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SabyContactsPage(BasePage):
    BASE_URL = "https://saby.ru"

    CONTACTS_MENU = (By.XPATH, "//span[text()='Контакты']")
    MORE_OFFICES = ( By.XPATH, "//a[contains(., 'офис') and contains(@href, '/contacts')]")
    TENSOR_BANNER = (By.XPATH, "//a[contains(@href, 'tensor.ru') and not(contains(@href, '/about'))]")

    def open(self):
        self.driver.get(self.BASE_URL)

    def go_to_contacts(self):
        contacts = self.find(self.CONTACTS_MENU)

        ActionChains(self.driver).move_to_element(contacts).perform()
        self.wait.until(EC.visibility_of_element_located(self.MORE_OFFICES))
        self.click(self.MORE_OFFICES)

    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)
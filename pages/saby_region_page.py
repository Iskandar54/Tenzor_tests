from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class RegionPage(BasePage):
    BASE_URL = "https://saby.ru"

    CONTACTS_MENU = (By.XPATH, "//span[text()='Контакты']")
    MORE_OFFICES = ( By.XPATH, "//a[contains(., 'офис') and contains(@href, '/contacts')]")

    CURRENT_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    PARTNERS_LIST = (By.XPATH, "//*[@id='contacts_list']//div[@data-qa='item'][.//*[contains(text(), '+7') or contains(text(), '@')]]")
    
    REGION_CHOOSER = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser.ml-16.ml-xm-0")
    REGION_PANEL = (By.CLASS_NAME, "sbis_ru-Region-Panel__list-l")
    KAMCHATKA_REGION = (By.XPATH, "//span[@title='Камчатский край']")

    def open(self):
        self.driver.get(self.BASE_URL)

    def go_to_contacts(self):
        contacts = self.find(self.CONTACTS_MENU)

        ActionChains(self.driver).move_to_element(contacts).perform()
        self.wait.until(EC.visibility_of_element_located(self.MORE_OFFICES))
        self.click(self.MORE_OFFICES)

    def get_current_region(self):
        region_elements = self.wait.until(EC.presence_of_all_elements_located(self.CURRENT_REGION))
        
        for element in region_elements:
            if element.text and element.text.strip():
                return element.text.strip()
        
        if region_elements:
            self.wait.until(lambda driver: region_elements[0].text and region_elements[0].text.strip())
            return region_elements[0].text.strip()
        
        raise Exception("Не удалось найти регион")

    def get_partners(self):
        return self.find_all(self.PARTNERS_LIST)

    def change_region_to_kamchatka(self):
        region_chooser = self.find(self.REGION_CHOOSER)
        region_chooser.click()
        self.wait.until(EC.visibility_of_element_located(self.REGION_PANEL))
        
        kamchatka_element = self.wait.until(EC.element_to_be_clickable(self.KAMCHATKA_REGION))
        #kamchatka_element.click()
        self.driver.execute_script("arguments[0].click();", kamchatka_element)

        self.wait.until(EC.invisibility_of_element_located(self.REGION_PANEL))
        self.wait.until(lambda driver: "Камчатский" in self.get_current_region())

    def get_page_title(self):
        return self.driver.title
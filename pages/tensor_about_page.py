from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TensorAboutPage(BasePage):

    WORK_SECTION_IMAGES = (By.CSS_SELECTOR, "div.tensor_ru-About__block3-image-wrapper img")

    def get_all_images_dimensions(self):
        images = self.wait.until(EC.visibility_of_all_elements_located(self.WORK_SECTION_IMAGES))
        for img in images:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", img)
        return [(img.size['width'], img.size['height']) for img in images]

    def all_images_same_size(self):
        dimensions = self.get_all_images_dimensions()
        return all(dim == dimensions[0] for dim in dimensions)

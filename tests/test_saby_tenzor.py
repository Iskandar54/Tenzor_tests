from pages.saby_contacts_page import SabyContactsPage
from pages.tensor_main_page import TensorMainPage
from pages.tensor_about_page import TensorAboutPage
from utils.logger import logger

def test_height_and_width(driver):
    saby = SabyContactsPage(driver)
    logger.info("Открываем сайт Saby")
    saby.open()
    logger.info("Переходим в контакты")
    saby.go_to_contacts()
    logger.info("Кликаем Тензор банер")
    saby.click_tensor_banner()

    driver.switch_to.window(driver.window_handles[1])
    logger.info("Переключаемся на новую вкладку")

    tensor = TensorMainPage(driver)
    assert tensor.is_people_power_block_visible()
    logger.info("Кликаем на подробнее")
    tensor.click_more_details()
    assert "tensor.ru/about" in driver.current_url

    about = TensorAboutPage(driver)
    logger.info("Проверяем размеры")
    assert about.all_images_same_size()
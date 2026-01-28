from pages.saby_region_page import RegionPage
from utils.logger import logger

def test_saby_region_partners(driver):
    region = RegionPage(driver)
    region.open()
    region.go_to_contacts()

    current_region = region.get_current_region()
    logger.info(f"Текущий регион: {current_region}")
    assert current_region, "Регион не определился"
    partners = region.get_partners()
    logger.info(f"Найдено партнеров: {len(partners)}")
    assert len(partners) > 0, "Список партнеров пуст"

    region.change_region_to_kamchatka()
    logger.info("Меняем регион на Камчатский край")
    new_region = region.get_current_region()
    assert "Камчатский" in new_region

    new_partners = region.get_partners()
    logger.info(f"Партнеры Камчасткого края: {len(new_partners)}")
    assert len(new_partners) > 0, "Не найдено партнеров в Камчатском крае"

    new_url = region.get_current_url().lower()
    assert "kamchatskij-kraj" in new_url, f"URL не содержит информацию о Камчатском крае: {new_url}"

    new_title = region.get_page_title()
    assert "Камчатский" in new_title, f"Title не содержит информацию о Камчатском крае: {new_title}"
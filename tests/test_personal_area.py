from pages.personal_area_page import PersonalAreaPage
import allure

class TestPersonalArea:
    
    @allure.title('Проверка открытия личного кабинета по кнопке в хэдере')
    def test_personal_area_opening_via_header(self, driver, create_login_user):
        driver = create_login_user["driver"]
        personal_area = PersonalAreaPage(driver)
        personal_area.click_on_personal_area_button_header()

        assert personal_area.history_order_item_is_visible()

    @allure.title('Проверка открытия истории заказов в личном кабинете')
    def test_opening_order_history(self, driver, create_login_user_with_an_order):
        driver = create_login_user_with_an_order["driver"]
        personal_area = PersonalAreaPage(driver)
        personal_area.click_on_personal_area_button_header()
        personal_area.click_on_order_history_link()
        assert personal_area.history_order_item_is_visible()

    @allure.title('Проверка разлогина пользователя')
    def test_user_logout(self, driver, create_login_user_with_an_order):
        driver = create_login_user_with_an_order["driver"]
        personal_area = PersonalAreaPage(driver)

        personal_area.click_on_personal_area_button_header()
        assert personal_area.logout_button_visibility()

        personal_area.click_on_logout_button()
        assert personal_area.login_section_is_visible()
        


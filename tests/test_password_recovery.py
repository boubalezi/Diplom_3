from pages.auth_page import AuthPage
import allure

class TestPasswordRecovery:

    @allure.title('Проверка скрытия/показа пароля для восстановления')
    def test_recover_password_visibility(self, driver):
        auth_page = AuthPage(driver)
        auth_page.click_on_personal_area_button_header()
        auth_page.scroll_to_recover_password_link()
        auth_page.click_on_recover_password_link()
        auth_page.fill_email_field()
        auth_page.click_on_recover_password_button()
        auth_page.fill_password_field()

        assert auth_page.is_password_hidden()

        auth_page.click_show_hide_password_button()

        assert auth_page.is_password_visible()



from pages.base_page import BasePage
from locators.auth_page import LoginPageLocators, ResetPasswordPageLocators, ForgotPasswordPageLocators
from locators.personal_area_page import PersonalAreaPageLocators
from src.data import UserData
import allure

class AuthPage(BasePage):

    @allure.step("Клик по кнопке 'Личный кабинет' в хедере")
    def click_on_personal_area_button_header(self):
        self.click_element(PersonalAreaPageLocators.PERSONAL_AREA_BUTTON)

    @allure.step("Прокрутка до ссылки восстановления пароля")
    def scroll_to_recover_password_link(self):
        self.scroll_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Клик по ссылке восстановления пароля")
    def click_on_recover_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Заполнить поле email")
    def fill_email_field(self):
        email = UserData.generate_email()
        self.enter_text(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_on_recover_password_button(self):
        self.click_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step("Заполнить поле password")
    def fill_password_field(self):
        password = UserData.generate_random_number()
        self.enter_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_hide_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)
    
    @allure.step("Получение значения из поля пароля")
    def get_password_value(self):
        password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("value")
    
    @allure.step("Проверка, что пароль скрыт")
    def is_password_hidden(self):
        password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("type") == "password"

    @allure.step("Проверка, что пароль виден")
    def is_password_visible(self):
        password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("type") == "text"


    

    


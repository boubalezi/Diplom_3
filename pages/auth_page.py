from pages.base_page import BasePage
from locators.auth_page import LoginPageLocators, ResetPasswordPageLocators, ForgotPasswordPageLocators
from locators.personal_area_page import PersonalAreaPageLocators
from src.data import UserData

class AuthPage(BasePage):

    def click_on_personal_area_button_header(self):
        self.click_element(PersonalAreaPageLocators.PERSONAL_AREA_BUTTON)

    def scroll_to_recover_password_link(self):
        self.scroll_to_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def click_on_recover_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def fill_email_field(self):
        email = UserData.generate_email()
        self.enter_text(LoginPageLocators.EMAIL_FIELD, email)

    def click_on_recover_password_button(self):
        self.click_element(ForgotPasswordPageLocators.RECOVER_PASSWORD_BUTTON)

    def fill_password_field(self):
        password = UserData.generate_random_number()
        self.enter_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    def click_show_hide_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)
    
    def get_password_value(self):
        password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("value")
    
    def is_password_hidden(self):
        password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("type") == "password"

    def is_password_visible(self):
        password_field = self.find_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return password_field.get_attribute("type") == "text"


    

    


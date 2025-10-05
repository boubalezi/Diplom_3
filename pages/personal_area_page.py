from pages.base_page import BasePage
from locators.auth_page import LoginPageLocators
from locators.personal_area_page import PersonalAreaPageLocators


class PersonalAreaPage(BasePage):

    def click_on_personal_area_button_header(self):
        self.click_element(PersonalAreaPageLocators.PERSONAL_AREA_BUTTON)

    def fill_in_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL_FIELD, email)

    def fill_in_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_FIELD, password)

    def click_on_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def click_on_order_history_link(self):
        self.click_element(PersonalAreaPageLocators.ORDER_HISTORY_LINK)

    def click_on_logout_button(self):
        self.click_element(PersonalAreaPageLocators.LOGOUT_BUTTON)
    
    def logout_button_visibility(self):
        return self.wait_until_visible(PersonalAreaPageLocators.LOGOUT_BUTTON)
    
    def history_order_item_is_visible(self):
        return self.wait_until_visible(PersonalAreaPageLocators.ORDER_HISTORY_LINK)

    def login_section_is_visible(self):
        return self.wait_until_visible(LoginPageLocators.LOGIN_SECTION)

    

    





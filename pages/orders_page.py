from pages.base_page import BasePage
from locators.main_order_list_page import MainOrderListLocators
from locators.personal_area_page import PersonalAreaPageLocators, PersonalOrderLocators



class TestOrderPage(BasePage):

    def click_on_personal_area_button_header(self):
        self.click_element(PersonalAreaPageLocators.PERSONAL_AREA_BUTTON)

    def click_on_first_order(self):
        self.click_element(PersonalOrderLocators.FIRST_ORDER_IN_LIST)

    def get_order_number(self):
        element = self.wait_until_visible(PersonalOrderLocators.FIRST_ORDER_IN_LIST)
        return element.text.strip()
    
    def get_order_number_from_main_order_list(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDER_NUMBER_IN_MAIN_ORDERS_LIST)
        text = element.text.strip()
        return text.splitlines()[0]
    
    def get_amount_of_orders_all_time(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDERS_DONE_ALL_TIME)
        text = element.text.strip()
        return text
    
    def get_amount_of_orders_today(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDERS_DONE_TODAY)
        text = element.text.strip()
        return text
    
    def get_order_number_in_progress(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDER_IN_PROGRESS)
        text = element.text.strip()
        return text

    def scroll_to_amount_orders_today(self):
        self.scroll_to_element(MainOrderListLocators.ORDERS_DONE_TODAY)

    def order_modal_visibility(self):
        element = self.wait_until_visible(PersonalOrderLocators.ORDER_NUMBER_IN_MODAL)
        return element.text.strip()
    
    def close_order_modal(self):
        self.click_element(PersonalOrderLocators.ORDER_MODAL_CLOSE_BUTTON)

    def history_order_item_is_visible(self):
        return self.wait_until_visible(PersonalAreaPageLocators.ORDER_HISTORY_LINK)
    
    def click_on_order_history_link(self):
        self.click_element(PersonalAreaPageLocators.ORDER_HISTORY_LINK)

    def order_modal_clickability(self):
        self.wait_until_clickable(PersonalOrderLocators.ORDER_MODAL_CLOSE_BUTTON)

    def click_on_order_list_button(self):
        self.click_element(MainOrderListLocators.ORDERS_LIST_BUTTON)

    

    


from pages.base_page import BasePage
from locators.main_order_list_page import MainOrderListLocators
from locators.personal_area_page import PersonalAreaPageLocators, PersonalOrderLocators
import allure


class OrderPage(BasePage):

    @allure.step("Клик по кнопке 'Личный кабинет' в хэдере")
    def click_on_personal_area_button_header(self):
        self.click_element(PersonalAreaPageLocators.PERSONAL_AREA_BUTTON)

    @allure.step("Клик по первому заказу в списке")
    def click_on_first_order(self):
        self.click_element(PersonalOrderLocators.FIRST_ORDER_IN_LIST)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        element = self.wait_until_visible(PersonalOrderLocators.FIRST_ORDER_IN_LIST)
        return element.text.strip()
    
    @allure.step("Получение номера заказа из основного списка заказов")
    def get_order_number_from_main_order_list(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDER_NUMBER_IN_MAIN_ORDERS_LIST)
        text = element.text.strip()
        return text.splitlines()[0]
    
    @allure.step("Получение общего количества заказов за всё время")
    def get_amount_of_orders_all_time(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDERS_DONE_ALL_TIME)
        text = element.text.strip()
        return text
    
    @allure.step("Получение общего количества заказов за сегодня")
    def get_amount_of_orders_today(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDERS_DONE_TODAY)
        text = element.text.strip()
        return text
    
    @allure.step("Получение номера заказа в работе")
    def get_order_number_in_progress(self):
        element = self.wait_until_visible(MainOrderListLocators.ORDER_IN_PROGRESS)
        text = element.text.strip()
        return text

    @allure.step("Прокрутка к элементу с количеством заказов за сегодня")
    def scroll_to_amount_orders_today(self):
        self.scroll_to_element(MainOrderListLocators.ORDERS_DONE_TODAY)

    @allure.step("Проверка видимости модального окна заказа")
    def order_modal_visibility(self):
        element = self.wait_until_visible(PersonalOrderLocators.ORDER_NUMBER_IN_MODAL)
        return element.text.strip()
    
    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        self.click_element(PersonalOrderLocators.ORDER_MODAL_CLOSE_BUTTON)

    @allure.step("Ожидание видимости ссылки на историю заказов")
    def history_order_item_is_visible(self):
        return self.wait_until_visible(PersonalAreaPageLocators.ORDER_HISTORY_LINK)
    
    @allure.step("Клик по ссылке 'История заказов'")
    def click_on_order_history_link(self):
        self.click_element(PersonalAreaPageLocators.ORDER_HISTORY_LINK)

    @allure.step("Ожидание кликабельности кнопки закрытия модального окна заказа")
    def order_modal_clickability(self):
        self.wait_until_clickable(PersonalOrderLocators.ORDER_MODAL_CLOSE_BUTTON)

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_order_list_button(self):
        self.click_element(MainOrderListLocators.ORDERS_LIST_BUTTON)

    

    


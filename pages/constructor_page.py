from pages.base_page import BasePage
from locators.constructor_page import ConstructorPageLocators
from locators.main_order_list_page import MainOrderListLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



class TestMainOrderPage(BasePage):

    def click_on_order_list_button(self):
        self.click_element(MainOrderListLocators.ORDERS_LIST_BUTTON)

    def order_list_title_visibility(self):
        return self.wait_until_visible(MainOrderListLocators.ORDER_LIST_TITLE)

    def orders_done_counter_visibility(self):
        return self.wait_until_visible(MainOrderListLocators.ORDERS_DONE_TITLE)

    def click_on_constructor_button(self):
        self.click_element(ConstructorPageLocators.CONSTRUCTOR_BUTTON)
    
    def create_burger_title_visibility(self):
        return self.wait_until_visible(ConstructorPageLocators.CREATE_BURGER_TITLE)

    def click_on_buns_item_by_index(self, index=0):
        buns = self.driver.find_elements(*ConstructorPageLocators.BUNS_LIST)
        if len(buns) > index:
            element = buns[index]
            self.driver.execute_script("arguments[0].click();", element)
        else:
            raise IndexError(f"Bun with index {index} not found")
        
    def click_on_souces_button(self):
        self.click_element(ConstructorPageLocators.SOUCES_BUTTON)

    def click_on_toppings_button(self):
        self.click_element(ConstructorPageLocators.TOPPINGS_BUTTON)

    def click_on_buns_button(self):
        self.click_element(ConstructorPageLocators.BUNS_BUTTON)
        
    def order_details_visibility(self):
        return self.wait_until_visible(ConstructorPageLocators.DETAILS_MODAL)
    
    def click_on_order_details_exit_button(self):
        self.click_element(ConstructorPageLocators.EXIT_DETAILS_MODAL_BUTTON)

    def drag_bun_to_constructor_by_index(self, index=0):
        buns = self.driver.find_elements(*ConstructorPageLocators.BUNS_LIST)
        if len(buns) <= index:
            raise IndexError(f"Bun with index {index} not found")

        bun_element = buns[index]
        constructor_target = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TARGET)

        actions = ActionChains(self.driver)
        actions.click_and_hold(bun_element)
        actions.move_to_element(constructor_target)
        actions.release().perform() 

    def drag_souce_to_constructor_by_index(self, index=0):
        souce = self.driver.find_elements(*ConstructorPageLocators.SOUCES_LIST)
        if len(souce) <= index:
            raise IndexError(f"Souce with index {index} not found")

        souce_element = souce[index]
        constructor_target = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TARGET)

        actions = ActionChains(self.driver)
        actions.click_and_hold(souce_element)
        actions.move_to_element(constructor_target)
        actions.release().perform() 

    def drag_topping_to_constructor_by_index(self, index=0):
        topping = self.driver.find_elements(*ConstructorPageLocators.TOPPINGS_LIST)
        if len(topping) <= index:
            raise IndexError(f"Souce with index {index} not found")

        topping_element = topping[index]
        constructor_target = self.driver.find_element(*ConstructorPageLocators.CONSTRUCTOR_TARGET)

        actions = ActionChains(self.driver)
        actions.click_and_hold(topping_element)
        actions.move_to_element(constructor_target)
        actions.release().perform() 
    
    def click_on_place_order(self):
        self.click_element(ConstructorPageLocators.PLACE_ORDER_BUTTON)
    
    def order_success_modal_visibility(self):
        return self.wait_until_visible(ConstructorPageLocators.ORDER_IDENTIFIER_TEXT)

    def get_ingredient_counters(self):
        counters = {}
        ingredient_names = ["Булки", "Соусы", "Начинки"]

        for name in ingredient_names:
            try:
                xpath = ConstructorPageLocators.INGREDIENT_COUNTER.format(ingredient_name=name)
                element = self.driver.find_element(By.XPATH, xpath)
                counters[name] = int(element.text.strip()) if element.text.strip().isdigit() else 0
            except Exception:
                counters[name] = 0

        return counters
    
    def get_counter_for_category(self, category_index: int = 1, ingredient_index: int = 1) -> int:
        xpath = ConstructorPageLocators.COUNTER_FOR_CATEGORY.format(
            category_index=category_index, ingredient_index=ingredient_index
        )
        element = self.wait_until_visible((By.XPATH, xpath))
        text = element.text.strip()
        return int(text) if text.isdigit() else 0
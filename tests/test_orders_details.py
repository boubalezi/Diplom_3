from pages.orders_page import OrderPage
import allure

class TestOrderElements:

    @allure.title('Проверка открытия ленты заказов через кнопку в хэдере')
    def test_order_details_modal(self, create_login_user_with_an_order):
        driver = create_login_user_with_an_order["driver"]
        order = OrderPage(driver)

        order.click_on_personal_area_button_header()
        order.click_on_order_history_link()
        order.click_on_first_order()

        assert order.order_modal_visibility()

    @allure.title('Проверка наличия созданного заказа в ленте заказов')
    def test_order_exist_in_main_order_list(self, create_login_user_with_an_order):
        driver = create_login_user_with_an_order["driver"]
        order = OrderPage(driver)
        order.click_on_personal_area_button_header()
        order.click_on_order_history_link()
        order.get_order_number()
        modal_number = order.get_order_number()
        modal_number_only = modal_number.split('\n')[0]
       
        order.click_on_order_list_button()
       
        history_number = order.get_order_number_from_main_order_list()
        history_number_only = history_number.strip()    
        assert modal_number_only == history_number_only

    @allure.title('Проверка увеличения каунтера заказов за все время после создания нового заказа')
    def test_orders_done_counter_all_time(self, create_order):
        driver = create_order["driver"]
        order = OrderPage(driver)

        order.click_on_order_list_button()
        amount_of_orders_done_before = order.get_amount_of_orders_all_time()

        create_order["make_order"]()

        driver.refresh()
        order.click_on_order_list_button()
        amount_of_orders_done_after = order.get_amount_of_orders_all_time()

        assert int(amount_of_orders_done_after) == int(amount_of_orders_done_before) + 1

    @allure.title('Проверка увеличения каунтера заказов за сегодня после создания нового заказа')
    def test_orders_done_counter_today(self, create_order):
        driver = create_order["driver"]
        order = OrderPage(driver)

        order.click_on_order_list_button()
        order.scroll_to_amount_orders_today()
        amount_of_orders_done_before = order.get_amount_of_orders_today()

        create_order["make_order"]()
    
        driver.refresh()
        order.click_on_order_list_button()

        order.scroll_to_amount_orders_today()
        amount_of_orders_done_after = order.get_amount_of_orders_today()

        assert int(amount_of_orders_done_after) == int(amount_of_orders_done_before) + 1

    @allure.title('Проверка, что новый заказ имеет статус "В работе"')
    def test_order_number_has_in_progress_status(self, create_order):
        driver = create_order["driver"]
        order = OrderPage(driver)

        create_order["make_order"]()
    
        driver.refresh()
        order.click_on_personal_area_button_header()
        order.click_on_order_history_link()

        order_number = order.get_order_number().split('\n')[0]

        order.click_on_order_list_button()
 
        order_number_in_progress = order.get_order_number_in_progress()

        assert order_number_in_progress in order_number

                
            









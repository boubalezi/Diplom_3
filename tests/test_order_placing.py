from pages.constructor_page import MainOrderPage
import allure

class TestOrderCreation:

    @allure.title('Проверка открытия ленты заказов по кнопке в хэдере')
    def test_order_list_opening_via_button(self, driver):
        order = MainOrderPage(driver)

        order.click_on_order_list_button()
        assert order.order_list_title_visibility()
        assert order.orders_done_counter_visibility()

    @allure.title('Проверка открытия конструктора по кнопке в хэдере')
    def test_constructor_opening_via_button(self, driver):
        order = MainOrderPage(driver)

        order.click_on_order_list_button()
        order.click_on_constructor_button()
        assert order.create_burger_title_visibility()

    @allure.title('Проверка открытия модального окна с деталями ингредиента')
    def test_ingredient_details(self, driver):
        order = MainOrderPage(driver)
        order.click_on_buns_item_by_index()

        assert order.order_details_visibility()
        order.click_on_order_details_exit_button()

        assert order.create_burger_title_visibility()

    @allure.title('Проверка увеличения каунтера ингредиента при добавлении его в заказ')
    def test_ingredient_counter(self, driver):
        order = MainOrderPage(driver)

        initial_bun_counter = order.get_counter_for_category(category_index=1, ingredient_index=1)
        order.drag_bun_to_constructor_by_index(0)

        assert order.get_counter_for_category(category_index=1, ingredient_index=1) == initial_bun_counter + 2

        order.click_on_souces_button()
        initial_souce_counter = order.get_counter_for_category(category_index=2, ingredient_index=1)
        order.drag_souce_to_constructor_by_index(0)
        assert order.get_counter_for_category(category_index=2, ingredient_index=1) == initial_souce_counter + 1

        order.click_on_toppings_button()
        initial_topping_counter = order.get_counter_for_category(category_index=3, ingredient_index=1)
        order.drag_topping_to_constructor_by_index(0)
        assert order.get_counter_for_category(category_index=3, ingredient_index=1) == initial_topping_counter + 1


    @allure.title('Проверка создания заказа для авторизованного пользователя')
    def test_order_creation_for_auth_user(self, create_login_user):
        driver = create_login_user["driver"]
        order = MainOrderPage(driver)

        order.get_counter_for_category(category_index=1, ingredient_index=1)
        order.drag_bun_to_constructor_by_index(0)
        order.click_on_souces_button()
        order.drag_souce_to_constructor_by_index(0)
        order.click_on_toppings_button()
        order.drag_topping_to_constructor_by_index(0)
        order.click_on_place_order()
        assert order.order_success_modal_visibility()

   
   
        






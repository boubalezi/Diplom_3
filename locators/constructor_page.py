from selenium.webdriver.common.by import By

class ConstructorPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    CREATE_BURGER_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    BUNS_LIST = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul[1]//a")
    BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']")
    SOUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']")
    SOUCES_LIST = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul[1]//a")
    TOPPINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")
    TOPPINGS_LIST = (By.XPATH, "//h2[text()='Начинки']/following-sibling::ul[1]//a")
    DETAILS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]//h2[text()='Детали ингредиента']")
    EXIT_DETAILS_MODAL_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")
    CONSTRUCTOR_TARGET = (By.CSS_SELECTOR, "div.constructor-element_pos_top")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'button_button_type_primary') and text()='Оформить заказ']")
    ORDER_IDENTIFIER_TEXT = (By.XPATH, "//p[contains(@class,'text_type_main-medium') and contains(text(),'идентификатор заказа')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title__2L34m')]")
    COUNTER_FOR_CATEGORY = '//*[@id="root"]/div/main/section[1]/div[2]/ul[{category_index}]/a[{ingredient_index}]/div[1]/p'
    INGREDIENT_COUNTER = "//h2[text()='{ingredient_name}']/following-sibling::p[contains(@class,'counter_counter__num')]"






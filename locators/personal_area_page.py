from selenium.webdriver.common.by import By

class PersonalAreaPageLocators:

    PERSONAL_AREA_BUTTON = (By.XPATH, "//a[@href='/account']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_LIST_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//a")

class PersonalOrderLocators:

    FIRST_ORDER_IN_LIST = (By.XPATH, "(//li[contains(@class,'OrderHistory_listItem__')])[1]//a")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//div[contains(@class,'Modal_orderBox__')]/p[contains(@class,'text_type_digits-default')]")
    ORDER_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")



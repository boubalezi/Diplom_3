from selenium.webdriver.common.by import By

class MainOrderListLocators:

    ORDER_NUMBER_IN_MAIN_ORDERS_LIST = (By.CSS_SELECTOR, ".OrderFeed_list__OLh59 > li:first-child p.text_type_digits-default")
    ORDERS_DONE_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    ORDERS_DONE_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class,'OrderFeed_number')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]//li")

    ORDERS_LIST_BUTTON = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    ORDER_LIST_TITLE = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    ORDERS_DONE_TITLE = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]")
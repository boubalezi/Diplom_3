from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    LOGIN_SECTION = (By.XPATH, "//div[contains(@class, 'Auth_login')]")

class ForgotPasswordPageLocators:
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

class ResetPasswordPageLocators:
    SHOW_HIDE_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    PASSWORD_TOGGLE_VISIBLE = (By.XPATH, "//div[contains(@class, 'input_type_text')]//div[contains(@class, 'input__icon-action')]")
    PASSWORD_TOGGLE_HIDDEN = (By.XPATH, "//div[contains(@class, 'input_type_password')]//div[contains(@class, 'input__icon-action')]")



    
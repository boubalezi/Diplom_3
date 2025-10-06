from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.timeout = timeout

    def navigate(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.wait_until_clickable(locator)
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.wait_until_visible(locator)
        element = self.find_element(locator)
        element.send_keys(text)

    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
       
    def wait_until_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def scroll_to_element(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def switch_to_new_window(self, original_window, url_contains=None):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.number_of_windows_to_be(2))
        new_window = next(handle for handle in self.driver.window_handles if handle != original_window)
        self.driver.switch_to.window(new_window)
        if url_contains:
            WebDriverWait(self.driver, self.timeout).until(expected_conditions.url_contains(url_contains))

    def get_current_url(self):
        return self.driver.current_url

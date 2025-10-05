import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from src.data import Urls, UserData, INGREDIENT_IDS
from pages.personal_area_page import PersonalAreaPage
import requests


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService()
        browser = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    browser.get(Urls.BASE_URL)
    yield browser
    browser.quit()

@pytest.fixture
def create_new_user_with_an_order():
    user_data = UserData.generate_user()

    response = requests.post(f'{Urls.BASE_URL}{Urls.USER_CREATION_ENDPOINT}', json = user_data)
    body = response.json()
    access_token = body.get("accessToken")

    if access_token:
        headers = {"Authorization": access_token}
        order_data = {
    "ingredients": [
        INGREDIENT_IDS["bun"][0],
        INGREDIENT_IDS["sauce"][0]
    ]
}
        requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', json=order_data, headers=headers)

    yield {
        "user_data": user_data,
        "access_token": body.get("accessToken")
    }

    if access_token:
        headers = {"Authorization": access_token}
    requests.delete(f'{Urls.BASE_URL}{Urls.CHANGE_USER_ENDPOINT}', headers=headers)

@pytest.fixture
def create_login_user(driver):
    user_data = UserData.generate_user()

    response = requests.post(f'{Urls.BASE_URL}{Urls.USER_CREATION_ENDPOINT}', json=user_data)
    access_token = response.json().get("accessToken")

    driver.get(f"{Urls.BASE_URL}/login")  
    login_page = PersonalAreaPage(driver)
    login_page.fill_in_email(user_data["email"])
    login_page.fill_in_password(user_data["password"])
    login_page.click_on_login_button()

    yield {
        "driver": driver,
        "user_data": user_data,
        "access_token": access_token
    }

    if access_token:
        headers = {"Authorization": access_token}
        requests.delete(f'{Urls.BASE_URL}{Urls.CHANGE_USER_ENDPOINT}', headers=headers)


@pytest.fixture
def create_login_user_with_an_order(driver):
    user_data = UserData.generate_user()

    response = requests.post(f'{Urls.BASE_URL}{Urls.USER_CREATION_ENDPOINT}', json=user_data)
    access_token = response.json().get("accessToken")

    driver.get(f"{Urls.BASE_URL}/login")  
    login_page = PersonalAreaPage(driver)
    login_page.fill_in_email(user_data["email"])
    login_page.fill_in_password(user_data["password"])
    login_page.click_on_login_button()

    if access_token:
        headers = {"Authorization": access_token}
        order_data = {
            "ingredients": [
                INGREDIENT_IDS["bun"][0],
                INGREDIENT_IDS["sauce"][0]
            ]
        }
        requests.post(f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}', json=order_data, headers=headers)

    yield {
        "driver": driver,
        "user_data": user_data,
        "access_token": access_token
    }

    if access_token:
        headers = {"Authorization": access_token}
        requests.delete(f'{Urls.BASE_URL}{Urls.CHANGE_USER_ENDPOINT}', headers=headers)


@pytest.fixture
def create_order(create_login_user):
    access_token = create_login_user["access_token"]

    def _make_order():
        headers = {"Authorization": access_token}
        order_data = {
            "ingredients": [
                INGREDIENT_IDS["bun"][0],
                INGREDIENT_IDS["sauce"][0]
            ]
        }
        response = requests.post(
            f'{Urls.BASE_URL}{Urls.CREATE_ORDER_ENDPOINT}',
            json=order_data,
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    return {
        "driver": create_login_user["driver"],
        "user_data": create_login_user["user_data"],
        "access_token": access_token,
        "make_order": _make_order
    }
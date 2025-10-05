import random
from faker import Faker

fake = Faker()

class UserData:

    @staticmethod
    def generate_email():
        return fake.email()
    
    @staticmethod
    def generate_random_name():
        return fake.name()

    @staticmethod
    def generate_random_number():
        return str(random.randint(100000, 999999))
    
    @staticmethod
    def generate_user():
        return {
            "email": UserData.generate_email(),
            "password": UserData.generate_random_number(),
            "name": UserData.generate_random_name()
        }

class Urls:

    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    USER_CREATION_ENDPOINT = "/api/auth/register"
    CHANGE_USER_ENDPOINT = "/api/auth/user"
    CREATE_ORDER_ENDPOINT = "/api/orders"
    LOGIN_ENDPOINT = "/api/auth/login"

INGREDIENT_IDS = {
    "bun": [
        "61c0c5a71d1f82001bdaaa6d",  
        "61c0c5a71d1f82001bdaaa6c",  
    ],
    "main": [
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa70",
        "61c0c5a71d1f82001bdaaa71",
        "61c0c5a71d1f82001bdaaa6e",
        "61c0c5a71d1f82001bdaaa76",
        "61c0c5a71d1f82001bdaaa77",
        "61c0c5a71d1f82001bdaaa78",
        "61c0c5a71d1f82001bdaaa79",
        "61c0c5a71d1f82001bdaaa7a",
    ],
    "sauce": [
        "61c0c5a71d1f82001bdaaa72",
        "61c0c5a71d1f82001bdaaa73",
        "61c0c5a71d1f82001bdaaa74",
        "61c0c5a71d1f82001bdaaa75",
    ],

    "invalid_hash": [
        "61c0c5a71d1f82001baaa72",
        "61c0c5a71d1f8201bdaaa73",
        "61c0c5a71d1f82001baaa74",
        "61c0c5a71d1f82001ybdaaa75",
    ]
}




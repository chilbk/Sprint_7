import requests
import string
import random

class LoginCourierAPI:
    RESOURCE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_LOGIN = RESOURCE_URL + '/api/v1/courier/login'
#Метод для ввода логина и пароля
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(self.COURIER_LOGIN, json=payload)
        return response
# Метод, который генерирует рандомный логин и пароль
    def login_with_random_credentials(self, length=10):
# Чуть переделал метод из generate_random_string. Решил попробовать поиграть с модулем string
# По идее string.ascii_lowercase вводит случайные буквы латинского алфавита
        login = ''.join(random.choices(string.ascii_lowercase, k=length))
# string.ascii_letters - вводит случайные буквы латинского алфавита разного регистра
# string.digits - вводит случайные цифры от 0 до 9
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        response = self.login_courier(login, password)
        return response
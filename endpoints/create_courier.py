import requests
import random
import string

class CourierAPI:
    RESOURCE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATE = RESOURCE_URL + '/api/v1/courier'
#Генерирует случайную строку. Нужно для создание логина и пароля
    def generate_random_string(self, length=10):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
#Отправляет запрос на создание курьера с переданными данными
    def create_courier(self, login="emotional", password="burnout", first_name="critical"):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(self.COURIER_CREATE, json=payload)
        return response
#Отправляет запрос на создание курьера с данными, которыми были сгенерированы автоматически с помощью метода generate_random_string
    def register_new_courier(self):
        login = self.generate_random_string()
        password = self.generate_random_string()
        first_name = self.generate_random_string()
        response = self.create_courier(login, password, first_name)
        return response.status_code, login, password, first_name

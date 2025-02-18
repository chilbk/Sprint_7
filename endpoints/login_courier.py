import requests
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

    def login_with_random_credentials(self, length=10):
        login = ''.join(random.choices(string.ascii_lowercase, k=length))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

        response = self.login_courier(login, password)  # Отправляем запрос с этими данными
        return response
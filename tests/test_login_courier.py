import requests
from courier_api import CourierAPI
from login_courier import LoginCourierAPI


class TestCourierLogin:
# Сетап параметров
    def setup_method(self):
        self.courier_api = CourierAPI()
        self.login_api = LoginCourierAPI()
        self.setup_courier()
# Сетап курьера
    def setup_courier(self):
        response = self.courier_api.create_courier("emotional", "burnout", "critical")
        return response
# В данном тесте проверяется возможность входа. Также мы проверяем в нем, что у курьера есть id
    def test_successful_login(self):
        response = self.login_api.login_courier("emotional", "burnout")
        assert response.status_code == 200
        assert "id" in response.json(), "У данного клиента нет id"
# В данном тесте мы входим без пароля
    def test_login_missing_password(self):
        response = self.login_api.login_courier("emotional", "")
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
# В данном тесте мы входим без логина
    def test_login_missing_login(self):
        response = self.login_api.login_courier("", "burnout")
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
# В данном тесте мы используем неверный логин и пароль
    def test_login_invalid_credentials(self):
        response = self.login_api.login_courier("wrong_login", "wrong_password")
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

import pytest
import requests
from create_courier import CourierAPI


class TestCourierAPI:
    @pytest.fixture(scope="function")
    def courier_api(self):
        return CourierAPI()
# Создание курьера
    def test_create_courier_success(self, courier_api):
        login = courier_api.generate_random_string()
        password = courier_api.generate_random_string()
        first_name = courier_api.generate_random_string()
        response = courier_api.create_courier(login, password, first_name)
        assert response.status_code == 201, f"Ошибка: {response.text}"
        delete_response = courier_api.delete_courier(login, password)
        assert delete_response == 200 , f"Ошибка удаления"
# Создание курьера без логина
    def test_create_courier_missing_login(self, courier_api):
        password = courier_api.generate_random_string()
        first_name = courier_api.generate_random_string()
        response = courier_api.create_courier(None, password, first_name)
        assert response.status_code == 400, f"Ошибка: {response.text}"
# Создание курьера без пароля
    def test_create_courier_missing_password(self, courier_api):
        login = courier_api.generate_random_string()
        first_name = courier_api.generate_random_string()
        response = courier_api.create_courier(login, None, first_name)
        assert response.status_code == 400, f"Ошибка: {response.text}"
# Создание дубликата
    def test_create_courier_duplicate(self, courier_api):
        login = courier_api.generate_random_string()
        password = courier_api.generate_random_string()
        first_name = courier_api.generate_random_string()

        courier_api.create_courier(login, password, first_name)  # Первое создание
        response = courier_api.create_courier(login, password, first_name)  # Повторное создание
        assert response.status_code == 409, f"Ошибка: {response.text}"
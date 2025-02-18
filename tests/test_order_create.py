import pytest
from order_api import OrderAPI

class TestOrderCreation:
    def setup_method(self):
        self.order_api = OrderAPI()
# Хз, делают ли такую параметризацию, но выглядит как будто компактно и не так нагруженно
    @pytest.mark.parametrize("order_key, expected_status, expected_message", [
        ("valid_order", 201, None),  # Успешный заказ с одним цветом
        ("empty_fields", 400, "Недостаточно данных для создания заказа"),  # Пустые поля
        ("invalid_phone", 400, "Некорректный номер телефона"),  # Неверный номер телефона
        ("both_colors", 201, None)  # Успешный заказ с двумя цветами
    ])
# В этом тесте мы берем данные из словаря, отправляем запрос и сверяем статус ответа
    def test_create_order(self, order_key, expected_status, expected_message):
        order_data = self.order_api.ORDERS[order_key]
        response = self.order_api.create_order(order_data)
        assert response.status_code == expected_status

        # А вот тут ищем track в полученном json'е
        if expected_status == 201:
            assert "track" in response.json(), "В ответе нет поля 'track'. Заказ не был создан."
        else:
            assert response.json().get("message") == expected_message, "Ошибка обработки"
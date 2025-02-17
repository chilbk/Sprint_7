import pytest
from unittest.mock import patch
from order_api import OrderAPI

class TestOrderCreation:
    def setup_method(self):
        self.order_api = OrderAPI()

    @pytest.mark.parametrize(
        "first_name, last_name, address, apartment, phone, weight, delivery_date, comment, color",
        [
            ("Naruto", "Uchiha", "Konoha, 142 apt.", "4", "+7 800 355 35 35", 5, "2020-06-06", "Saske, come back to Konoha", ["BLACK"]),
            ("", "", "", "", "", "", "", "", None),
            ("Naruto", "Uchiha", "Konoha, 142 apt.", "4", "12345", 5, "2025-02-20", "Позвоните заранее", None),
            ("Naruto", "Uchiha", "Konoha, 142 apt.", "4", "+7 800 355 35 35", 5, "2020-06-06", "Naruto, come back to Konoha", []),
            ("Naruto", "Uchiha", "Konoha, 142 apt.", "4", "+7 800 355 35 35", 5, "2020-06-06", "Sakura, come back to Konoha", ["BLACK", "GREY"]),
        ]
    )
    @patch("order_api.requests.post")
    def test_order_creation(self, mock_post, first_name, last_name, address, apartment, phone, weight, delivery_date, comment, color):
# Попробовал использовать моки в данном случае, чтобы не зависеть от метода
        if first_name == "" or last_name == "" or address == "" or phone == "":
            mock_post.return_value.status_code = 400
            mock_post.return_value.json.return_value = {"message": "Недостаточно данных для создания заказа"}
        elif phone == "12345":
            mock_post.return_value.status_code = 400
            mock_post.return_value.json.return_value = {"message": "Некорректный номер телефона"}
        else:
            mock_post.return_value.status_code = 201
            mock_post.return_value.json.return_value = {"track": 12345 if color else 67890}
# Вызывается метод для создания заказа
        response = self.order_api.create_order(
            first_name, last_name, address, apartment, phone, weight, delivery_date, comment, color
        )

        if response.status_code == 201:
            assert "track" in response.json(), "В ответе нет поля 'track'. Заказ не был создан."
        else:
            assert "message" in response.json(), "Ошибка обработки"
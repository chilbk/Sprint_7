import pytest
from unittest.mock import patch
from order_list import OrderListAPI

class TestOrderListAPI:
    def setup_method(self):
        self.order_list_api = OrderListAPI()

# В данном тесте запрос идет с дефолтными параметрами
    @patch("order_list.requests.get")
    def test_get_orders_default(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"orders": [], "page": 0, "total": 0}
        response = self.order_list_api.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert response.json()["page"] == 0

# В данном тесте запрос отдаст активные и завершенные заказы у курьера
    @pytest.mark.parametrize("courier_id", [1, 2, 3])
    @patch("order_list.requests.get")
    def test_get_orders_with_courier_id(self, mock_get, courier_id):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"orders": [{"id": 101, "courierId": courier_id}]}
        response = self.order_list_api.get_orders(courier_id=courier_id)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert response.json()["orders"][0]["courierId"] == courier_id
# В данном тесте выдача происходит по станциям метро
    @patch("order_list.requests.get")
    def test_get_orders_with_nearest_station(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"orders": [{"id": 102, "nearestStation": ["1", "2"]}]}
        response = self.order_list_api.get_orders(nearest_station=["1", "2"])

        assert response.status_code == 200
        assert "orders" in response.json()
        assert response.json()["orders"][0]["nearestStation"] == ["1", "2"]
# В данном тесте мы передаем незаполненные атрибуты. По идее нам должен вернуться пустой список, так как все параметры необязательные
    @patch("order_list.requests.get")
    def test_get_orders_empty_request(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"orders": []}
        response = self.order_list_api.get_orders()

        assert response.status_code == 200
        assert response.json()["orders"] == []
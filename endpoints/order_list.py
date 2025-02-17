import requests

class OrderListAPI:
    RESOURCE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDER_CREATE_OR_LIST = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
#Метод отправляет GET-запрос для получения списка заказов
    def get_orders(self, courier_id=None, nearest_station=None, limit=30, page=0):
        params = {
            "limit": limit,
            "page": page
        }
        if courier_id is not None:
            params["courierId"] = courier_id
        if nearest_station is not None:
            params["nearestStation"] = nearest_station

        response = requests.get(self.ORDER_CREATE_OR_LIST, params=params)
        return response
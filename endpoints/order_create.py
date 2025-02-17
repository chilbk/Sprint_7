import requests
class OrderAPI:
#Метод на создание заказа
    RESOURCE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDER_CREATE_OR_LIST = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    def create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment,
                     color=None):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
        }

        if color:
            payload["color"] = color

        response = requests.post(self.ORDER_CREATE_OR_LIST, json=payload)
        return response
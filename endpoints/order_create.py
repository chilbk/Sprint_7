import requests

class OrderAPI:
    RESOURCE_URL = 'https://qa-scooter.praktikum-services.ru'
    ORDER_CREATE_OR_LIST = RESOURCE_URL + '/api/v1/orders'

# valid_order - валидный случай
# empty_fields - случай, когда мы передаем пустой лист
# invalid_phone - случай с неверным телефоном
# both_colors - случай, когда мы используем сразу 2 цвета
    ORDERS = {
        "valid_order": {
            "firstName": "Naruto",
            "lastName": "Uzumaki",
            "address": "Konoha, 142 apt.",
            "metroStation": "4",
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2025-02-20",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        },
        "empty_fields": {
            "firstName": "",
            "lastName": "",
            "address": "",
            "metroStation": "",
            "phone": "",
            "rentTime": "",
            "deliveryDate": "",
            "comment": "",
            "color": None
        },
        "invalid_phone": {
            "firstName": "Sasuke",
            "lastName": "Uchiha",
            "address": "Hidden Leaf",
            "metroStation": "4",
            "phone": "12345",  # Некорректный номер
            "rentTime": 3,
            "deliveryDate": "2025-02-22",
            "comment": "Naruto, come back to Konoha",
            "color": ["GREY"]
        },
        "both_colors": {  # Новый тестовый кейс
            "firstName": "Kakashi",
            "lastName": "Hatake",
            "address": "Konoha, 23 apt.",
            "metroStation": "7",
            "phone": "+7 999 555 35 35",
            "rentTime": 2,
            "deliveryDate": "2025-03-15",
            "comment": "Sakura, come back to Konoha",
            "color": ["GREY", "BLACK"]
        }
    }

    def create_order(self, order_data):
        response = requests.post(self.ORDER_CREATE_OR_LIST, json=order_data)
        return response
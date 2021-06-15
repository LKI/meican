import unittest

from meican.models import Address, Dish, Restaurant, Tab


class ModelsTests(unittest.TestCase):
    def setUp(self):
        self.address_data = {
            "uniqueId": "address_uid",
            "address": "address",
            "pickUpLocation": "pick_up_location",
        }
        self.tab_data = {
            "title": "title",
            "targetTime": 1500000000000,
            "status": "CLOSED",
            "userTab": {
                "uniqueId": "tab_uid",
                "corp": {
                    "addressList": [self.address_data],
                },
            },
        }
        self.restaurant_data = {
            "uniqueId": "restaurant_uid",
            "name": "restaurant_name",
            "open": False,
            "rating": "5",
            "tel": "010-12345678",
            "latitude": "30.123456",
            "longitude": "30.123456",
        }
        self.dish_data = {
            "id": "12345",
            "name": "dish_name",
            "priceString": "20.00",
        }

    def test_address(self):
        address = Address(self.address_data)
        self.assertEqual("address_uid address", "{}".format(address))

    def test_tab(self):
        tab = Tab(self.tab_data)
        self.assertEqual("CLOSED 2017-07-14 title", "{}".format(tab))

    def test_restaurant(self):
        rest = Restaurant(Tab(self.tab_data), self.restaurant_data)
        self.assertEqual("restaurant_name", "{}".format(rest))

    def test_dish(self):
        dish = Dish(Restaurant(Tab(self.tab_data), self.restaurant_data), self.dish_data)
        self.assertEqual("dish_name", "{}".format(dish))

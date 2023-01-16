import unittest
import requests
from unittest import TestCase

# python -m unittest tests/test_main.py

from main import YandexDisk, geo_logs, numbers, ya

class TestReturnDict(TestCase):
    def test_is_dict(self):
        res = geo_logs()
        dict_2 = {}
        for i in res:
            for land, city in i.values():
                dict_2.setdefault(city, land)
        self.assertIsInstance(res, list)
        self.assertIsInstance(dict_2, dict)
        self.assertIn('Россия', dict_2)
        self.assertNotIn('Индия', dict_2)
        self.assertNotIn('Португалия', dict_2)
        self.assertNotIn('Франция', dict_2)

class TestReturnNumbers(TestCase):
    def test_numbers(self):
        res = numbers()
        self.assertIsInstance(res, list)
        for i in res:
            self.assertIsInstance(i, int)

class TestReturnYa(TestCase):
    def test_ya(self):
        res = ya()
        self.assertIs('yandex', res)

class TestReturnFolder(TestCase):
    def test_folder(self):
        res = YandexDisk('y0_AgAAAAADtb4EAADLWwAAAADRTNTYskAI1MKzQx-Ba_W_lz5GFJx1LTk') 
        res.create_folder('Testing')
        set = res.get_folder('/Testing')
        self.assertEqual(set.status_code, 200)
        self.assertNotEqual(set.status_code, 201)
        self.assertNotEqual(set.status_code, 400)
        self.assertNotEqual(set.status_code, 401)
        self.assertNotEqual(set.status_code, 403)
        self.assertNotEqual(set.status_code, 404)
        self.assertNotEqual(set.status_code, 406)
        self.assertNotEqual(set.status_code, 409)
        self.assertNotEqual(set.status_code, 413)
        self.assertNotEqual(set.status_code, 423)
        self.assertNotEqual(set.status_code, 429)
        self.assertNotEqual(set.status_code, 503)
        self.assertNotEqual(set.status_code, 507)
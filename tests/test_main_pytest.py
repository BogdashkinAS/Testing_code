import pytest
import requests
from main import YandexDisk, geo_logs, numbers, ya

@pytest.mark.parametrize('set', ['Индия', 'Португалия', 'Франция'])
def test_is_dict(set):
    res = geo_logs()
    for visit in res:
        assert 'Россия' == list(visit.values())[0][1]
        assert set != list(visit.values())[0][1]
        
def test_numbers():
    res = numbers()
    assert isinstance(res, list)
    for i in res:
        assert isinstance(i, int)

def test_ya():
    res = ya()
    assert 'yandex' == res

@pytest.mark.parametrize('set', [201, 400, 401, 403, 404, 406, 409, 413, 423, 429, 503, 507])
def test_folder(set):
    res = YandexDisk('') # введите токен c ЯндексДиска
    res.create_folder('Testing')
    set = res.get_folder('/Testing')
    assert set.status_code == 200
    assert set.status_code != set
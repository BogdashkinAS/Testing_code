import requests

class YandexDisk:
        
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        requests.put(f'{folder_url}?path={path}', headers=headers)

    def get_folder(self, path):
        folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        return requests.get(f'{folder_url}?path={path}', headers=headers) 

def geo_logs():
    geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

    country = 'Россия'
    geo_logs_2 = []
    for i in range(len(geo_logs)):
      if country in str(geo_logs[i]):
        geo_logs_2.append(geo_logs[i])
    return geo_logs_2

def numbers():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    all_ids = set()
    for value in ids.values():
      all_ids.update(set(value))
    return(list(all_ids))

def ya():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    values = stats.values()
    max_values = 0
    a = list(values)
    for i in range(len(a)):
        if max_values <= int(a[i]):
            max_values = int(a[i])
    for id, course in enumerate(stats):
        if max_values == stats.get(course):
            return course
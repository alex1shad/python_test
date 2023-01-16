import requests


with open('token.txt', 'rt') as file:
    token = file.read()

url_ya = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': f'OAuth {token}'}
folder_name = 'new folder'


def yad_new_folder(folder_name):
    url_new_folder = f'{url_ya}?path={folder_name}'
    resp = requests.put(url=url_new_folder, headers=headers).status_code
    return resp


def test_token():
    url_test = 'https://cloud-api.yandex.net/v1/disk'
    resp_token = requests.get(url=url_test, headers=headers).status_code
    assert resp_token == 200, 'Токен введен неверно'


def test_name_folder():
    assert yad_new_folder(folder_name) != 409, 'Имя папки занято'

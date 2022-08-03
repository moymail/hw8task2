import os
import requests
TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get('href', '')
        result = requests.put(href, data=open(path_to_file, 'rb'))
        if result.status_code == 201:
            print('Загрузка завершена')
        else:
            print(f'Ошибка загрузки! Код ошибки: {result.status_code}')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = os.path.join(os.getcwd(), 'text.txt')
    print(path_to_file)
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload('text.txt')

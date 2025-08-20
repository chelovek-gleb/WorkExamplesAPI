from dotenv import load_dotenv
import os
import requests

load_dotenv() # подгружаем секреты из .env

base_url = 'https://mls.platform.big3.ru/api/chat_history/' # Базовый URL

"""Параметры для разных запросов"""
rooms_key = 'chat-rooms/rooms/'
users_key = 'users/'
groups_key = 'groups/'
room_id = '5/'
delete_key = 'clear_history/'

"""Заголовок для запросов"""
headers = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("API_TOKEN")
        }

class RoomActions():
    """Методы взаимодействия с комнатой: создание, удаление, закрепление, открепление"""

    def pin_room(self):
        """метод закрепления комнаты"""
        post_resource_pin = 'pin/'
        post_url = f'{base_url}{rooms_key}{room_id}{post_resource_pin}' # урл для закрепления
        print(f'Отправляем запрос на: {post_url}')
        result_post = requests.post(post_url, headers=headers) # отправка запроса, тело не нужно
        print(f'Получен ответ: {result_post.json()}')
        return result_post
    
    def unpin_room(self):
        """метод открепления комнаты"""
        post_resource_unpin = 'unpin/'
        post_url = f'{base_url}{rooms_key}{room_id}{post_resource_unpin}' # урл для открепления
        print(f'Отправляем запрос на: {post_url}')
        result_post = requests.post(post_url, headers=headers) # отправка запроса, тело не нужно
        print(f'Получен ответ: {result_post.json()}')
        return result_post
    
    def check_group_member(self):
        """запрос всех групп помощников"""
        get_url = f'{base_url}{groups_key}' # урл для запроса
        print(f'Отправляем запрос на: {get_url}')
        result_get = requests.get(get_url, headers=headers) # отправка запроса
        print(f'Получен ответ: {result_get.json()}')
        return result_get
    
    def clear_history(self):
        """метод очистки истории чата"""
        delete_resource = 'clear_history/'
        delete_url = f'{base_url}{rooms_key}{room_id}{delete_resource}' # урл для запроса
        print(f'Отправляем запрос на: {delete_url}')
        result_delete = requests.delete(delete_url, headers=headers) # отправка запроса
        print(f'Получен ответ: {result_delete.json()}')
        return result_delete
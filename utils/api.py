from dotenv import load_dotenv
import os
import requests

load_dotenv()

base_url = 'https://mls.platform.big3.ru/api/chat_history/' # Базовый URL

"""Параметры для разных запросов"""
rooms_key = 'chat-rooms/rooms/'
users_key = 'users/'
groups_key = 'groups/'
room_id = '5/'
delete_key = 'clear_history/'

headers = {
            "Content-Type": "application/json",
            "Authorization": os.getenv("API_TOKEN")
        }

class RoomActions():
    """Методы взаимодействия с комнатой: создание, удаление, закрепление, открепление"""

    def pin_room(self):

        post_resource_pin = 'pin/'
        post_url = f'{base_url}{rooms_key}{room_id}{post_resource_pin}'
        print(f'Отправляем запрос на: {post_url}')
        result_post = requests.post(post_url, headers=headers)
        print(f'Получен ответ: {result_post.json()}')
        return result_post
    
    def unpin_room(self):
        
        post_resource_unpin = 'unpin/'
        post_url = f'{base_url}{rooms_key}{room_id}{post_resource_unpin}'
        print(f'Отправляем запрос на: {post_url}')
        result_post = requests.post(post_url, headers=headers)
        print(f'Получен ответ: {result_post.json()}')
        return result_post
    
    def check_group_member(self):

        get_url = f'{base_url}{groups_key}'
        print(f'Отправляем запрос на: {get_url}')
        result_get = requests.get(get_url, headers=headers)
        print(f'Получен ответ: {result_get.json()}')
        return result_get
    
    def clear_history(self):

        delete_resource = 'clear_history/'
        delete_url = f'{base_url}{rooms_key}{room_id}{delete_resource}'
        print(f'Отправляем запрос на: {delete_url}')
        result_delete = requests.delete(delete_url, headers=headers)
        print(f'Получен ответ: {result_delete.json()}')
        return result_delete
"""
Нужен механизм reply - ответа на Сообщение
https://testit.big3.ru/projects/26143/tests/26882
"""


import os
import pytest
from dotenv import load_dotenv # подгружаем секреты из .env

load_dotenv()

@pytest.mark.order(4) #тест выполняется 4 в очереди
@pytest.mark.parametrize("wss_actions", ["wss://mls.platform.big3.ru/ws/room/5/"], indirect=True) #параметризация теста, отдается ссылка в фикстуру для установки соединения
def test_reply_wss_message(wss_actions):

    TOKEN = os.getenv("WSS_TOKEN") #подтягиваем токет из .env

    # пейлоад для авторизации в wss
    auth_payload = {
        "message_type": "auth",
        "data": {"token": TOKEN}
    }

    # тело сообщения в wss
    message_payload = {
        "message_type": "chat_message",
        "data": {
            "text": "Тестовое сообщение",
            "uuid": "2e01fc71-157b-4f5f-a1bd-5c0f1e75dd01",
            "files": [],
            "params": {}
        }
    }

    # Авторизация
    print("\nАвторизация:")
    wss_actions.send_message(auth_payload) # отправляем сообщение с авторизаций
    auth_messages = wss_actions.receive_messages() # получаем сообщения авторизации
    print(f"Всего сообщений: {len(auth_messages)}\n")

    # Первое сообщение
    print("\nОтправляем первое сообщение:")
    wss_actions.send_message(message_payload) # отправляем первое сообщение
    print("\nПолучаем ответ на первое сообщение:")
    all_messages = wss_actions.receive_messages() # получаем ответ на сообщение
    print(f"Всего сообщений: {len(all_messages)}\n")

    picked_message = all_messages[2] # выбираем сообщение, в котором содержится ответ
    check_picked_message = picked_message.get('data', {}).get('id') # выбираем поле id

    # Ответ на выбранное сообщение
    message_text = "Ответ на сообщение"
    message_payload_reply = {
        "message_type": "chat_message",
        "data": {
            "text": message_text,
            "uuid": "2e01fc71-157b-4f5f-a1bd-5c0f1e75dd01",
            "files": [],
            "params": {},
            "reply_to": check_picked_message
        }
    }
    print("\nОтправляем ответ на сообщение:")
    wss_actions.send_message(message_payload_reply) # отправляем сообщение

    print("\nПолучаем ответ на второе сообщение:")
    all_messages = wss_actions.receive_messages()  # получаем ответ на сообщение
    picked_message_second = all_messages[2] # выбираем сообщение, в котором содержится ответ
    thread_history = picked_message_second.get('data', {}).get('thread_history', []) # выбираем поле thread_history
    thread_history_text = thread_history[0].get('text') # берем первый элемент из списка, который является словарем, и из него ключ text

    assert thread_history_text == message_text, 'Текст первого сообщения не совпадает со вторым!'
    print(f'Текст в ответном сообщении: "{thread_history_text}" совпадает с текстом первого сообщения: {message_text}')

    

"""
Нужны "сломанные" помощники для тестирования (группа Broken)
https://testit.big3.ru/projects/26143/tests/26759
"""

import os
import pytest
from dotenv import load_dotenv

load_dotenv() # подгружаем секреты из .env

@pytest.mark.order(6) #тест выполняется 6 в очереди
@pytest.mark.parametrize("wss_actions", ["wss://mls.platform.big3.ru/ws/chat/broken/"], indirect=True) #параметризация теста, отдается ссылка в фикстуру для установки соединения
def test_broken_helper(wss_actions):
    """Метод включает в себя фикстуру wss_actions которая получает wss_url и открывает соединение, в конце теста закрывает"""

    TOKEN = os.getenv("WSS_TOKEN2") #подтягиваем токет из .env

    # пейлоад для авторизации в wss
    auth_payload = {
        "message_type": "auth",
        "data": {"token": TOKEN}
    }

    # тело сообщения в wss
    message_payload = {
    "message_type": "chat_message",
    "data": {
        "text": "Какие поля есть на данной форме списка?",
    
        "params": {
        "Перун": {
            "object_id": "200"
        }
        }
    }
    }

    # Авторизация
    wss_actions.send_message(auth_payload) # отправляем сообщение с авторизаций
    auth_messages = wss_actions.receive_messages() # получаем сообщения авторизации
    print(f"Всего сообщений: {len(auth_messages)}\n")

    # Первое сообщение
    wss_actions.send_message(message_payload) # отправляем первое сообщение
    all_messages = wss_actions.receive_messages() # получаем ответ на сообщение
    print(f"Всего сообщений: {len(all_messages)}\n")

    picked_message = all_messages[3] # выбираем сообщение, в котором содержится ответ
    check_picked_message = picked_message.get('data', {}).get('message') # выбираем поле message
    check_sender = picked_message.get('data', {}).get('sender') # выбираем поле sender
    print(f'check_picked_message= {check_picked_message}')
    assert check_sender == 'BrokenAssistant', 'Помощник не BrokenAssistant!' # проверяем правильный ли помощник ответил
    print(f'check_sender = {check_sender}')
   

    
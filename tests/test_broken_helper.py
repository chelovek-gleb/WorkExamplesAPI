"""
Нужны "сломанные" помощники для тестирования (группа Broken)
https://testit.big3.ru/projects/26143/tests/26759
"""


import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.order(6)
@pytest.mark.parametrize("wss_actions", ["wss://mls.platform.big3.ru/ws/chat/broken/"], indirect=True)
def test_reply_wss_message(wss_actions):
    TOKEN = os.getenv("WSS_TOKEN2")

    auth_payload = {
        "message_type": "auth",
        "data": {"token": TOKEN}
    }

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
    wss_actions.send_message(auth_payload)
    auth_messages = wss_actions.receive_messages()
    print(f"Всего сообщений: {len(auth_messages)}\n")

    # Первое сообщение
    wss_actions.send_message(message_payload)
    all_messages = wss_actions.receive_messages()
    print(f"Всего сообщений: {len(all_messages)}\n")

    picked_message = all_messages[3]
    check_picked_message = picked_message.get('data', {}).get('message')
    check_sender = picked_message.get('data', {}).get('sender')
    print(f'check_picked_message= {check_picked_message}')
    assert check_sender == 'BrokenAssistant', 'Помощник не BrokenAssistant!'
    print(f'check_sender = {check_sender}')
   

    
"""
Нужен механизм reply - ответа на Сообщение
https://testit.big3.ru/projects/26143/tests/26882
"""


import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.mark.order(4)
@pytest.mark.parametrize("wss_actions", ["wss://mls.platform.big3.ru/ws/room/5/"], indirect=True)
def test_reply_wss_message(wss_actions):
    TOKEN = os.getenv("WSS_TOKEN")

    auth_payload = {
        "message_type": "auth",
        "data": {"token": TOKEN}
    }

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
    wss_actions.send_message(auth_payload)
    auth_messages = wss_actions.receive_messages()
    print(f"Всего сообщений: {len(auth_messages)}\n")

    # Первое сообщение
    wss_actions.send_message(message_payload)
    all_messages = wss_actions.receive_messages()
    print(f"Всего сообщений: {len(all_messages)}\n")

    picked_message = all_messages[2]
    check_picked_message = picked_message.get('data', {}).get('id')

    # Ответ
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
    wss_actions.send_message(message_payload_reply)

    all_messages = wss_actions.receive_messages()
    picked_message_second = all_messages[2]
    thread_history = picked_message_second.get('data', {}).get('thread_history', [])
    thread_history_text = thread_history[0].get('text')

    assert thread_history_text == message_text, 'Текст первого сообщения не совпадает со вторым!'
    print(f'Текст в ответном сообщении: {thread_history_text} совпадает с текстом первого сообщения: {message_text}')

    

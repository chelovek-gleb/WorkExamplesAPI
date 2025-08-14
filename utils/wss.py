import websocket
import json
import time

class WssActions:
    def __init__(self):
        self.ws = None

    def connect(self, wss_url):
        self.ws = websocket.create_connection(wss_url, timeout=15)

    def send_message(self, payload: dict):
        if self.ws is None:
            raise RuntimeError("Соединение с WebSocket не установлено")
        self.ws.send(json.dumps(payload))

    def receive_messages(self, timeout_seconds=15):
        if self.ws is None:
            raise RuntimeError("Соединение с WebSocket не установлено")
        all_messages = []
        end_time = time.time() + timeout_seconds
        while time.time() < end_time:
            try:
                msg = self.ws.recv()
                msg_json = json.loads(msg)
                print("Текст:", msg_json)
                all_messages.append(msg_json)
            except websocket._exceptions.WebSocketTimeoutException:
                break
        return all_messages

    def close_connect(self):
        if self.ws:
            self.ws.close()
            print(' Соединение wss закрыто')
            self.ws = None

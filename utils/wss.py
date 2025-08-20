import websocket
import json
import time

class WssActions:
    """Класс действий с вебсокетом"""

    def __init__(self):
        self.ws = None # объект соединения с вебсокет, по умолчанию соединение с отключено

    def connect(self, wss_url):
        """Метод создания соединения с вебсокетом"""
        self.ws = websocket.create_connection(wss_url, timeout=15)

    def send_message(self, payload: dict):
        """Метод метод отправки сообщения через вебсокет с аргументов в виде тела сообщения"""
        if self.ws is None:  # Проверяем, есть ли соединение с вебсокет
            raise RuntimeError("Соединение с WebSocket не установлено") # если соединения нет, вызываем исключение с сообщением
        self.ws.send(json.dumps(payload)) # payload превращается в JSON-строку и отправляется

    def receive_messages(self, timeout_seconds=15):
        """метод получаения сообщений"""
        if self.ws is None:  # Проверяем, есть ли соединение с вебсокет
            raise RuntimeError("Соединение с WebSocket не установлено") # если соединения нет, вызываем исключение с сообщением
        all_messages = [] # пустой список для всех сообщений
        end_time = time.time() + timeout_seconds # переменная для таймаута
        while time.time() < end_time: # пока текущее время меньше чем заданный таймаут
            try:
                msg = self.ws.recv() # ждем сообщения от вебсокета
                msg_json = json.loads(msg) # преобразуем строку JSON в dict
                print("Текст:", msg_json)
                all_messages.append(msg_json) # добавляем сообщение в список
            except websocket._exceptions.WebSocketTimeoutException: # если мы не получили сообщение за заданное время - выходим из цикла
                break
        return all_messages

    def close_connect(self):
        if self.ws:
            """Метод закрытия соединения с вебсокетом"""
            self.ws.close()
            print('Соединение wss закрыто')
            self.ws = None

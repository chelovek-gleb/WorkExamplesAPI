import pytest
from utils.api import RoomActions
from utils.checking import Checking
from utils.wss import WssActions

@pytest.fixture
def room_actions():
    """Фикстура для RoomActions"""
    return RoomActions()

@pytest.fixture
def check():
    """Фикстура для Checking"""
    return Checking()

"""Фикстура с параметризацией. Получаем wss_url как request, устанавливает соединение, после чего его закрывает"""
@pytest.fixture
def wss_actions(request):
    wss_url = request.param
    actions = WssActions()
    actions.connect(wss_url)
    yield actions
    actions.close_connect()


"""
Нужен признак закрепления Комнаты
https://testit.big3.ru/projects/26143/tests/26886
"""
import pytest

"""Тест открепления комнаты"""
@pytest.mark.order(3)
def test_unpin_room(check, room_actions):

    json_field = 'is_pinned' # Ожидаемое значение ключа в json-ответе
    expected_value = False # Ожидаемое значение поля в json-ответе

    print('\nТест начинается')
    result = room_actions.unpin_room() # сохраняем ответ от метода закрепления комнаты
    check.check_status_code(result, 200) # проверяем успешный статус-код
    check.check_json_value(result, json_field, expected_value) # Проверяем есть ли ожидаемые ключ и значение в ответе
    print('Тест прошел успешно!')


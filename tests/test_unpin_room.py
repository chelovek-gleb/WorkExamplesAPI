"""
Нужен признак закрепления Комнаты
https://testit.big3.ru/projects/26143/tests/26886
"""
import pytest

@pytest.mark.order(3)
def test_unpin_room(check, room_actions):

    json_field = 'is_pinned'
    expected_value = False

    print('\nТест начинается')
    result = room_actions.unpin_room()
    check.check_status_code(result, 200)
    check.check_json_value(result, json_field, expected_value)
    print('Тест прошел успешно!')


"""
Нужен API-метод для очистки истории Пользователя
https://testit.big3.ru/projects/26143/tests/27045
"""
import pytest

@pytest.mark.order(5)
def test_clear_history(check, room_actions):

    json_field = 'status'
    expected_value = 'success'

    print('\nТест начинается')
    result = room_actions.clear_history()
    check.check_status_code(result, 200)
    check.check_json_value(result, json_field , expected_value)
    print('Тест прошел успешно!')



"""
Нужен API-метод для очистки истории Пользователя
https://testit.big3.ru/projects/26143/tests/27045
"""
import pytest

@pytest.mark.order(5) # тест выполнится первый в очереди
def test_clear_history(check, room_actions):

    json_field = 'status' # Ожидаемое значение ключа в json-ответе
    expected_value = 'success' # Ожидаемое значение поля в json-ответе

    print('\nТест начинается')
    result = room_actions.clear_history() # сохраняем ответ от метода закрепления комнаты
    check.check_status_code(result, 200)  # проверяем успешный статус-код
    check.check_json_value(result, json_field , expected_value) # Проверяем есть ли ожидаемые ключ и значение в ответе
    print('Тест прошел успешно!')



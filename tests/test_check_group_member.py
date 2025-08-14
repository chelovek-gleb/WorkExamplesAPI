"""
Нужен TaskSpecifier (для task_specifier_assistant)
https://testit.big3.ru/projects/26143/tests/26765
"""
import pytest

@pytest.mark.order(1)
@pytest.mark.parametrize('expected_value', ["Семаргл", 
    "BPMN",
    "Portal",
    "DataGenerator",
    "StatusBuilder",
    "TaskSpecifier"
    ])
def test_check_group_member(check, room_actions, expected_value):

    print('\nТест начинается')
    result = room_actions.check_group_member()
    check.check_status_code(result, 200)
    check.check_json_value_in_list(result, expected_value)
    print('Тест прошел успешно!')



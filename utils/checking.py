
class Checking():

    def check_status_code(self, result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    def check_json_value(self, result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        print(f'Получили значение поля: {field_name} : {check_info}')
        assert check_info == expected_value, 'Значение поля не соответствует ожидаемому'
        print('Значение поля соответствует ожидаемому')

    def check_json_value_in_list(self, result, expected_value):
        check = result.json()
        for key, value_list in check.items():
            if expected_value in value_list:
                print(f'{expected_value} имеется в группе {key}')
                return
        assert False, f'{expected_value} нет в списке!'
           

        


class Checking():
    """Класс с методами для проверок"""

    def check_status_code(self, result, status_code):
        """Метод для проверки статус кода"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f"Успешно! Статус код = {result.status_code}")

    def check_json_value(self, result, field_name, expected_value):
        """Метод для значения в json"""
        check = result.json()
        check_info = check.get(field_name)
        print(f'Получили значение поля: {field_name} : {check_info}')
        assert check_info == expected_value, 'Значение поля не соответствует ожидаемому'
        print('Значение поля соответствует ожидаемому')

    def check_json_value_in_list(self, result, expected_value):
        """Метод для значения json в списке"""
        check = result.json() # Получаем словарь ключ: список[]
        for key, value_list in check.items(): # перебираем все пары ключ: значение
            if expected_value in value_list: # ищем ожидаемое значение в каждом списке
                print(f'{expected_value} имеется в группе {key}')
                return
        assert False, f'{expected_value} нет в списке!'
           

        

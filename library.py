from typing import Union, Optional

number: int = 5


def get_ukrainian_coins(number: int, last_number=None) -> str:
    last_number = int(str(number)[-1])
    if number == 0 or number in range(5, 21) or last_number == 0:
        result = 'копійок'
    elif number == 1 or last_number == 1:
        result = 'копійка'
    elif number in [2, 3, 4] or last_number in [2, 3, 4]:
        result = 'копійки'
    else:
        result = 'копійок'

    return result


def get_ukrainian_hryvnas(number: int, last_number=None) -> str:
    last_number = int(str(number)[-1])
    if number == 0 or number in range(5, 21) or last_number == 0:
        result = 'гривень'
    elif number == 1 or last_number == 1:
        result = 'гривня'
    elif number in [2, 3, 4] or last_number in [2, 3, 4]:
        result = 'гривні'
    else:
        result = 'гривень'

    return result


def get_money(value: Union[float, int], x=None) -> str:
    x = str(value)
    value = x.split('.')
    if len(value[1]) > 2:
        value[1] = value[1][:2]
    if len(value[1]) == 1:
        value[1] = value[1] + '0'
    if value[1][0] == '0':
        value[1] = value[1][1:]
    result = (f'{value[0]} {get_ukrainian_hryvnas(int(value[0]))}, {value[1]} {get_ukrainian_coins(int(value[1]))}')
    return result
'''
Остаток, начиная с третьего числа после запятой, удаляется
'''


def is_hot_today(temp=30) -> str:
    if temp > 25:
        return ('Hot')
    else:
        return ('Not hot')


lambda_list = [lambda weather: ('Hot') if weather > 25 else ('Not hot')]


def get_numbers(value: bool = True):
    if value == True:
        lem1 = lambda x: (x * x) ** 0.5
        return lem1
    if value == False:
        lem2 = lambda x: (x * x) ** 0.5 * -1
        return lem2


def return_entered_number(need_int=False) -> Union[float, int]:
    while True:
        user_input = input()
        try:
            result = float(user_input)
            if need_int:
                return int(result)
            return result

        except ValueError:
            print('\nInvalid enter. Try again')

import library
from typing import Union, Optional

massege = ('Надана вами сумма:')


def get_deposite() -> str:
    x = input('Enter your sum on deposite: ')
    sum = (f'{massege}  {library.get_money(x)}')
    print(sum)
    return sum


get_deposite()

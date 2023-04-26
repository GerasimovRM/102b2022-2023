from typing import Union, List, Set, Dict


def func(x: Union[int, str], y: Union[int, str]) -> Union[int, str]:
    """
    Это моя функция для сложения двух чисел

    :param x: первое слагаемое
    :param y: второе слагаемое
    :return: сумма
    """
    return x + y


def func2(lst: List[str],
          b: Set[Union[int, float]],
          d: Dict[str, List[int]],
          a: int = 3):
    pass


# print(func(3, 3.5))
print(func2([1, 2, 3], {'342', '234'}, {'asd': [2, 2]}))
print(isinstance(1, int), type(1) == int)

lst = [1, 3, 5]
lst: List[int]
for item in lst:


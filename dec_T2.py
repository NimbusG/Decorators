import functools
import random
from math import sqrt
from typing import List, Generator

# Модифицируйте код декоратора prime_filter
def prime_filter(func:callable) -> List[int]:
    """Дан список целых чисел, возвращайте только простые целые числа"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        list_of_numbers= func(*args, **kwargs)
        return [number for number in list_of_numbers if type(number)==int and is_prime(number)]

    return wrapper



def is_prime(n:int)->bool:
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

@prime_filter
def numbers(from_num:int, to_num:int)->List[int]:
    return [num for num in range(from_num, to_num)]

# вывод для примера
print(numbers(from_num=2, to_num=20))

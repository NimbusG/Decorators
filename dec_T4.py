# Напишите декоратор retry:
#
# декоратор вызовает функцию, которая возвращает True/False для индикации успешного или неуспешного выполнения функции.
# При сбое декоратор должен подождать и повторить попытку выполнения функции. При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой.
# Если у декоратора заканчиваются попытки, он сдается и возвращает исключение
from functools import wraps
from time import sleep


def retry(max_retries:int, initial_delay:int=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for i in range(max_retries):
                print(f'Trying again to run function {func.__name__}, retries {i} from {max_retries}, {delay}s seconds')
                if func(*args, **kwargs):
                    return True
                sleep(delay)
                delay *= 2

            raise Exception('maximum number of retries exceeded')
        return wrapper
    return decorator

@retry(max_retries=3, initial_delay=1)
def test_function():
    return False


@retry(max_retries=3,initial_delay=1)
def check_for_name(name):
    if not name:
        print(f"not {name} return False")
        return False

    if name is isinstance(name,str):
        print(f"{name} is an instance of str")
        return name

    return name


    #if not isinstance(name, str):
    #    raise ValueError('name must be a string')
    #return name


#test_function()
#check_for_name('aa')

assert test_function() == True
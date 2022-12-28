# Создать декоратор simple_decorator с "хорошим поведением", то есть
import functools


# декоратор при котором происходит сохранение "магических" полей __name__  и  __doc__

# Должны проходиться тесты

def simple_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        print('__doc__ is: {}'.format(func.__doc__))
        return func(*args, **kwargs)
    return wrapper


@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        return func(*args, **kwargs)
    return you_will_never_see_this_name



@simple_decorator
def double(x):
    'Doubles a number.'
    return 2 * x

assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'

print(double(155))
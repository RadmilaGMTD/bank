from time import time


def log(filename_):
    def decorator(func):
        def wrapper(*args, **kwargs):
                try:
                    start_ = time()
                    result = func(*args, **kwargs)
                    end_ = time()
                    if filename_:
                        with open(filename_, 'a') as file:
                            file.write(f'{func.__name__} ok\n{func.__name__} start: {start_}\n{func.__name__} end: {end_}\n{func.__name__} result: {result}')
                    return f'{func.__name__} start: {start_}\n{func.__name__} end: {end_}\n{func.__name__} result: {result}'
                except Exception as e:
                    if filename_:
                        with open(filename_, 'a') as file:
                            file.write(f'{func.__name__} start: {start_}\n{func.__name__} end: {end_}\n{func.__name__} error: {e}. Inputs: {args, kwargs}')
                    return f'{func.__name__} start: {start_}\n{func.__name__} end: {end_}\n{func.__name__} error: {e}. Inputs: {args, kwargs}'
        return wrapper
    return decorator

filename_ = 'mylog.txt'
@log(filename_)
def my_function(x, y):
    return x + y

print(my_function(1, 2))
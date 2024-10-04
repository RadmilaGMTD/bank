def log(filename_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if filename_:
                    with open(filename_, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {e}. Inputs: {args, kwargs}')
                else:
                    print (f'{func.__name__} error: {e}. Inputs: {args, kwargs}')
            else:
                if filename_:
                    with open(filename_, 'a', encoding='utf-8') as file:
                        file.write(f'{func.__name__} ok\nstart {func.__name__}\nresult: {result}\nend {func.__name__}')
                else:
                    print (f'{func.__name__} ok\nstart {func.__name__}\nresult: {result}\nend {func.__name__}')

                return result
        return wrapper
    return decorator

filename_ = 'mylog.txt'
@log(filename_)
def my_function(x, y):
    return x + y

my_function(1, 5)
def type_logger(func):
    def wrapper(num):
        func(num)
        print(f'{num}: {type(num)}')
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(10)

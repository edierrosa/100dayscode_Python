def logging_decorator(func):
    def wrapper(*args):
        print(
            f"Function: {func.__name__}\nArguments: {args}\nOutput: {func(*args)}")
    return wrapper


@logging_decorator
def multiply(*args):
    result = 1
    for _ in args:
        result *= _
    return result


multiply(2, 2, 2)

import time
current_time = time.time()
print(current_time)


def speed_calc_decorator(func):
    def wrapper():
        time_start = time.time()
        func()
        time_end = time.time()
        print(
            f"Function: {func.__name__}\nExecution: {time_end - time_start} secs")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()

from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        time_before = time()
        func(*args, **kwargs)
        time_after = time()
        print(f"Времени потребовалось на расчет - {time_after - time_before}")
    return wrapper

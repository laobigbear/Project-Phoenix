import time
from functools import wraps

def timer(fn):
    """
    A decorator that measures the execution time of a function.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        duration = time.time() - start
        print(f"{fn.__name__} executed in {duration:.4f} seconds")
        return res
    return wrapper
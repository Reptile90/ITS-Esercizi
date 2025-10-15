
from typing import Callable

def cronometro(func:Callable):
    def wrapper(*args):
        import time
        start:float = time.time()
        func(*args)
        print(time.time()-start)
    return wrapper

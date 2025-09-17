


def bubblesort(lista:list)->list:

    for i in range(len(lista)):
        ordered = True
        for j in range (i +1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                





    return lista




import time
class Stopwatch:
    def __init__(self):
        self.start_time = 0.0
        self.end_time = 0.0
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self,exc_type,exc_value,traceback):

        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Elapsed time {elapsed_time:.8f} seconds")
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"An error occured {exc_value}")
            print(f"Traceback: {traceback}")
        return True
    



with Stopwatch():
    import random

    lista_numeri = random.sample(range(1, 101), 100)
    print(lista_numeri)
    print(bubblesort(lista_numeri))

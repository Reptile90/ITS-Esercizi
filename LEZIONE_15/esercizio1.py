'''Crea un context manager usando una classe

Definisci una classe FileManager che implementa un context manager che gestisce le risorse dei file.

Implementa appropriatamente la funzione __init__, __enter__ e la funzione  __exit__

Esempio di funzionamento:

Il context manager deve permettere di aprire il file, effettuare operazioni e chiudere la risorsa aperta.

with FileManager('example.txt', 'w') as f:

    f.write('Hello, world!')'''

class FileManager:
    def __init__(self, path:str, mode:str, coding:str ):
        self.path = path
        self.mode = mode
        self.coding = coding
    
    def __enter__(self):
        self.path = open(self.path,self.mode,self.coding)
    
    def __exit__(self, exc_type,exc_value, traceback):
        self.path.close()

        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")

        return False

with FileManager("example.txt","w","UTF-8") as f:
        f.write("Hello, World")
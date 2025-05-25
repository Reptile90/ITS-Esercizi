

class IntGEZ(int):
    #Tipo dato specializzato intero >= 0
    def __new__(cls, value: float | int | str | bool ):
        ret = int.__new__(cls, value) #prova a convertire v in un int

        if ret < 0:
            raise ValueError (f"The value {value} must be >= 0")
        return ret
        
if __name__ == "__main__":

    value1:IntGEZ = IntGEZ(30)
    print(value1)

    value2:IntGEZ = IntGEZ("rst")
    print(value2)
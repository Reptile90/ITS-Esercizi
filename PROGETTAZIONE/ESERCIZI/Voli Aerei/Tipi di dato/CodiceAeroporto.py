class CodiceAeroporto(str):
    def __new__(cls, value: int|float|str|bool):
        ret = str(value).upper().strip()
        if len(ret) != 3 or not ret.isalpha():
            raise ValueError (f"The value '{ret}' must be exactly 3 letters (IATA code)")
        return super().__new__(cls,ret)


if __name__ == "__main__":

    ca1:CodiceAeroporto = CodiceAeroporto("FCO")
    print(ca1)

    ca2:CodiceAeroporto = CodiceAeroporto("FGFGS")
    print(ca2)
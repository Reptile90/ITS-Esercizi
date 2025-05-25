import re

class CodiceVolo(str):
    def __new__(cls, value: int|float|str|bool):
        ret = str(value).upper().strip()
        pattern = re.compile(r"^[A-Z]{2,3}\d{1,4}$")
        if not pattern.fullmatch(ret):
            raise ValueError(f"The code '{ret}' must be 2-3 letters followed by 1-4 digits")
        return super().__new__(cls, ret)
    


if __name__ == "__main__":

    cv:CodiceVolo = CodiceVolo("AB021")
    print(cv)

    cv2:CodiceVolo = CodiceVolo("ABC32CC")
    print(cv2)
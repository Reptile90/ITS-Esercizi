class RealGZ(float):
    
    def __new__(cls, value: float | int | str | bool ):
        ret = float.__new__(cls, value) 

        if ret < 0:
            raise ValueError (f"The value {value} must be >= 0")
        return ret

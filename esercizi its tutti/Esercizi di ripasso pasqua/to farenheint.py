def convert_temperature(temp, to_fahrenheit=True) -> float:
    if not to_fahrenheit:
        celsius = (temp - 32) / 1.8
        return celsius
    else:
        fahrenheit = (temp * 1.8)+32
        return fahrenheit
    

print(convert_temperature(0))
print(convert_temperature(32, False))

    



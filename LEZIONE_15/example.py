PATH: str = "example.txt"

file = open(PATH,"r")

print(file.read())

file.close()

file = open("example.txt","a")
try:
    pass
except Exception as e:
    
finally:
    file.close()
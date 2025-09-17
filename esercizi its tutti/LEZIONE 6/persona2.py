class Persona:
    def __init__(self):
        self.name:str =""
        self.last_name:str =""
        self.age:int = 0

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.last_name}\nAge: {self.age}")   

#funzione che mi consenta di impostare il valore di self.name


    def setName(self,name:str)-> None:
        self.name = name


#funzione che mi consenta di impostare il valore di self.last_name

    def setLastname(self,last_name:str)->None:
        self.last_name = last_name


#funzione che mi consenta di impostare il valore di self.age

    def setAge(self,age:int)-> None:
        if  age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age    

# funzione che mi consenta di ritornare il valore di self.name
    def getName(self)->str:
        return self.name
#funzione che mi consenta di ritornare il valore di serl.last_name
    def getLastname(self)->str:
        return self.last_name 
#funzione che mi consenta di ritornare il valore di serlf.age
    def getAge(self)-> int:
        return self.age
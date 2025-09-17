class Person:
    def __init__(self, first_name:str|None, last_name:str|None):
        
        self.setName(self,first_name) 
        self.setLastName(self,last_name)
        self.setAge()
        
        
    def setName(self,first_name:str)->None:
        if isinstance(first_name,str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("IL nome inserito non è una stringa")
        
        
    def setLastName(self,last_name:str)->None:
        if isinstance(last_name,str):
            self.__last_name = last_name
        else:
            self.__first_name = None  
            print("Il cognome inserito non è una stringa")   
    
    def setAge(self,age:int)->None:
        if not self.setName() and not self.setLastName:
            self.__age = 0
        elif isinstance(age,int):
            self.__age = age
        else:
            print("L'età deve essere un numero intero")
        
        
    def getName(self)->str:
        return self.__first_name
    
    def getLastName(self)->str:
        return self.__last_name
    
    def getAge(self)->int:
        return self.__age
    
    
    def greet(self)->str:
        print(f"Ciao, sono {self.getName()}{self.getLastName()}! Ho {self.getAge()}anni!")
        
        
class Doctor(Person):
    def __init__(self, first_name, last_name, specialization:str, parcel:float):
        super().__init__(first_name, last_name)
        self.setSpecialization(specialization)
        self.setParcel(parcel)
        
        
    def setSpecialization(self,specialization:str)->None:
        if not isinstance(specialization,str):
            self.__specialization = None
            print("La specialization deve essere una stringa")
        self.__specialization = specialization
        
        
    def setParcel(self,parcel:float)->None:
        if not isinstance(parcel, float):
            self.__parcel = None
            print("La parcella inserita non è un float!")
        
    def getSpecialization(self)->str:
        return self.__specialization
    
    def getParcel(self)->float:
        return self.__parcel
    
    
    def isValidDoctor(self):
        if self.getAge() > 30:
            print(f"Doctor {self.getName()} {self.getLastName()} is valid!")
        else:
            print(f"Doctor {self.getName()} {self.getLastName()} is not valid!")
        
    def greet(self):
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")
        
        
        
class Patient(Person):
    def __init__(self, first_name, last_name, idCode:str):
        super().__init__(first_name, last_name)
        
        self.setIdCode(idCode)
        
        
    def setIdCode(self, idCode:str)->None:
        if isinstance(idCode,str):
            self.__idCode = idCode
        else:
            print("Il codice ID deve essree una stringa!")
            
    def getIdCode(self)->str:
        return self.__idCode
    
    def patientInfo(self):
        return (f"Paziente: {self.getName()} {self.getLastName()}"
                F"ID: {self.getIdCode()}")
        
        
class Fattura:
    def __init__(self, patient:list[Patient], doctor:Doctor):
        if doctor.isValidDoctor():
            self.__doctor = doctor
            self.__patient = patient
            self.__fatture:int = patient.count()
            self.__salary:int = 0
        else:
            self.__patient = None
            self.__doctor = None
            self.__fatture:int = None
            self.__salary:int = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido")
            
    def getSalary(self)->float:
        parcel = Doctor.getParcel()
        numPatient= self.__patient.count()
        
        salary = parcel * numPatient
        
        return salary
    
    
    def getFatture(self)->float:
        fatture = self.__patient.count()
        return fatture
    
    def addPatient(self, newPatient:Patient):
        if newPatient in self.__patient:
            self.__patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {Doctor.getName()} {Doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        else:
            print("Il paziente è già presente nella lista")
        
        
    def removePatient(self, idCode:str):
        for patient in self.__patient:
            if idCode not in patient:
                print("Paziente non trovato")
            else:
                self.__patient.remove(idCode)
                self.getFatture()
                self.getSalary()
                print(f"Alla lista del Dottor {Doctor.getLastName()}")
                
                
if __name__ == "__main__":
    doctor1:Doctor = Doctor("Claudio","Vellante","Medicina Nucleare",89.00)
    doctor2:Doctor = Doctor("Mario", "Rossi","Cardiologia",180.00)
    
    doctor1.setAge(56)
    doctor2.setAge(49)
    
    doctor1.greet()
    doctor2.greet()
    
    patient1:Patient = Patient("Anna","Verdi", "AV987")
    patient2:Patient = Patient("Lorenzo","Giallo","LG867")
    patient3:Patient = Patient("Federico","Bianco","FB342")
    patient4:Patient = Patient("Marcello","Neri", "MN003")
    
    fattura1 = Fattura(doctor1,[patient1,patient2,patient3])
    fattura2 = Fattura(doctor2,[patient4])
    
    
    print(f"Salario Dottor {doctor1.getLastName()}: {fattura1.getSalary()}")
    print(f"Salario Dottor {doctor2.getLastName()}: {fattura2.getSalary()}")
    
    fattura1.removePatient(patient2)
    
    fattura2.addPatient(patient2)
                
        
        
        
        
    
        
            
            
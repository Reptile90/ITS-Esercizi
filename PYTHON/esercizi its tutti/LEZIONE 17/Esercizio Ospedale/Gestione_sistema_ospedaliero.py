class Person:
    def __init__(self, first_name: str | None, last_name: str | None, age: int):
        self.setName(first_name)
        self.setLastName(last_name)
        self.setAge(age)

    def setName(self, first_name: str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = None
            print("Il nome inserito non è una stringa")

    def setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = None
            print("Il cognome inserito non è una stringa")

    def setAge(self, age: int) -> None:
        if isinstance(age, int):
            self.__age = age
        else:
            print("L'età deve essere un numero intero")

    def getName(self) -> str:
        return self.__first_name

    def getLastName(self) -> str:
        return self.__last_name

    def getAge(self) -> int:
        return self.__age

    def greet(self) -> None:
        print(f"Ciao, sono {self.getName()} {self.getLastName()}! Ho {self.getAge()} anni!")


class Doctor(Person):
    def __init__(self, first_name, last_name, age: int, specialization: str, parcel: float):
        super().__init__(first_name, last_name, age)
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    def setSpecialization(self, specialization: str) -> None:
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione deve essere una stringa")

    def setParcel(self, parcel: float) -> None:
        if isinstance(parcel, float):
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def getSpecialization(self) -> str:
        return self.__specialization

    def getParcel(self) -> float:
        return self.__parcel

    def isValidDoctor(self) -> bool:
        return self.getAge() > 30

    def greet(self) -> None:
        super().greet()
        print(f"Sono un medico specializzato in {self.getSpecialization()}")


class Patient(Person):
    def __init__(self, first_name, last_name, age: int, idCode: str):
        super().__init__(first_name, last_name, age)
        self.setIdCode(idCode)

    def setIdCode(self, idCode: str) -> None:
        if isinstance(idCode, str):
            self.__idCode = idCode
        else:
            print("Il codice ID deve essere una stringa!")

    def getIdCode(self) -> str:
        return self.__idCode

    def patientInfo(self) -> str:
        return f"Paziente: {self.getName()} {self.getLastName()} - ID: {self.getIdCode()}"


class Fattura:
    def __init__(self, doctor: Doctor, patients: list[Patient]):
        if doctor.isValidDoctor():
            self.__doctor = doctor
            self.__patients = patients
        else:
            self.__doctor = None
            self.__patients = []
            print("Non è possibile creare la fattura: il dottore non è valido")

    def getSalary(self) -> float:
        if self.__doctor:
            return self.__doctor.getParcel() * len(self.__patients)
        return 0.0

    def getFatture(self) -> int:
        return len(self.__patients)

    def addPatient(self, newPatient: Patient) -> None:
        if newPatient not in self.__patients:
            self.__patients.append(newPatient)
            print(f"Aggiunto paziente {newPatient.getIdCode()} al Dottor {self.__doctor.getLastName()}")
        else:
            print("Il paziente è già presente nella lista")

    def removePatient(self, id_code: str) -> None:
        for patient in self.__patients:
            if patient.getIdCode() == id_code:
                self.__patients.remove(patient)
                print(f"Paziente {id_code} rimosso.")
                return
        print("Paziente non trovato.")

                
if __name__ == "__main__":
    doctor1:Doctor = Doctor("Claudio","Vellante",55,"Medicina Nucleare",89.00)
    doctor2:Doctor = Doctor("Mario", "Rossi",59,"Cardiologia",180.00)
    
    doctor1.setAge(56)
    doctor2.setAge(49)
    
    doctor1.greet()
    doctor2.greet()
    
    patient1 = Patient("Anna", "Verdi", 34, "AV987")
    patient2:Patient = Patient("Lorenzo","Giallo",65,"LG867")
    patient3:Patient = Patient("Federico","Bianco",80,"FB342")
    patient4:Patient = Patient("Marcello","Neri", 45,"MN003")
    
    fattura1 = Fattura(doctor1,[patient1,patient2,patient3])
    fattura2 = Fattura(doctor2,[patient4])
    
    
    print(f"Salario Dottor {doctor1.getLastName()}: {fattura1.getSalary()}")
    print(f"Salario Dottor {doctor2.getLastName()}: {fattura2.getSalary()}")
    
    fattura1.removePatient(patient2)
    
    fattura2.addPatient(patient2)
    
    fattura1.getSalary()
    fattura2.getSalary()
    
    
    salario1 = fattura1.getSalary()
    salario2 = fattura2.getSalary()
    print(f"Guadagno ospedale: {salario1 + salario2}")
                
    
        
        
        
    
        
            
            
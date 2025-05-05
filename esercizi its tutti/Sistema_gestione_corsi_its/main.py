from Classe_Room import Room
from Classe_Building import Building
from Classe_Persona import Person
from Classe_Studente import Student
from Classe_Insegnante import Lecturer
from Classe_Gruppo import Group
from Classe_Corso import Course





# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")
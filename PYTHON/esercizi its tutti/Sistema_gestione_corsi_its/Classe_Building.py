from Classe_Room import Room

class Building:
    def __init__(self, name: str, address: str, floors: tuple):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    # metodi setter
    def set_name(self, name) -> None:
        if name:
            self.name = name
        else:
            raise ValueError("Il nome non può essere una stringa vuota")

    def set_address(self, address) -> None:
        if address:
            self.address = address
        else:
            raise ValueError("L'indirizzo non può essere una stringa vuota")

    def set_floors(self, floors) -> None:
        if not isinstance(floors, tuple) or len(floors) != 2:
            raise ValueError("I piani devono essere una tupla (min, max) con esattamente due elementi.")
        minFloor, maxFloor = floors
        if not isinstance(minFloor, int) or not isinstance(maxFloor, int):
            raise ValueError("Gli elementi della tupla 'floors' devono essere numeri interi.")
        if minFloor > maxFloor:
            raise ValueError("Il piano iniziale (min) non può essere maggiore del piano finale (max) nell'intervallo.")
        self.floors = floors

    def set_rooms(self, rooms) -> None:
        if not isinstance(rooms, list):
            raise ValueError("Le aule devono essere fornite in una lista.")
        for room in rooms:
            if not isinstance(room, Room):
                raise ValueError(f"L'elemento fornito '{room}' non è un oggetto 'Room'.")
        self.rooms = rooms

    # metodi getter
    def get_name(self) -> str:
        return self.name

    def get_address(self) -> str:
        return self.address

    def get_floors(self) -> tuple:
        return self.floors

    def get_rooms(self) -> list:
        return self.rooms

    # metodo per aggiungere un'aula
    def add_room(self, room: 'Room') -> None:
        if not isinstance(room, Room):
            raise TypeError("Puoi aggiungere solo oggetti di tipo 'Room'")

        minFloor, maxFloor = self.floors
        room_floor = room.get_floor()

        if minFloor <= room_floor <= maxFloor:
            if room not in self.rooms:
                self.rooms.append(room)
        else:
            pass

    # metodo per calcolare l'area totale
    def area(self) -> float:
        total_area = 0
        for room in self.rooms:
            try:
                total_area += room.get_area()
            except Exception as error:
                pass
        return total_area

    def __str__(self) -> str:
        return f"Building(name={self.name}, address={self.address}, floors={self.floors}, rooms={[room.get_id() for room in self.rooms]})"


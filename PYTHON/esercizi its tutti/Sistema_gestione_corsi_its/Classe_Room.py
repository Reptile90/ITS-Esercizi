
class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats

    # metodi setter
    def set_id(self, id) -> None:
        if id:
            self.id = id
        else:
            raise ValueError("L'id dell'aula non può essere una stringa vuota")

    def set_floor(self, floor) -> None:
        try:
            floor_int = int(floor)
            self.floor = floor_int
        except (ValueError, TypeError):
            raise ValueError("Il piano deve essere un numero intero valido.")

    def set_seats(self, seats) -> None:
        try:
            seats_int = int(seats)
            if seats_int >= 0:
                self.seats = seats_int
            else:
                raise ValueError("Il numero di posti non può essere negativo.")
        except (ValueError, TypeError):
            raise ValueError("Il numero di posti deve essere un numero intero valido non negativo.")

    # metodi getter
    def get_id(self) -> str:
        return self.id

    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats

    # metodo per calcolare l'area
    def get_area(self) -> float:
        seats = self.get_seats()
        if seats is not None:
            room_area = seats * 2.0
            if room_area.is_integer():
                return int(room_area)
            else:
                return room_area
        else:
            raise ValueError("Impossibile calcolare l'area: numero di posti non valido")





'''PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono (facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.

PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.'''

from typing import Any
def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    dictionary:dict[Any] = {"Profile": name, "Email": email, "telefono": telefono}

    return dictionary

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    
    if name is not None:
        dictionary["Profile"] = name
    if email is not None:
        dictionary["Email"] = email
    if telefono is not None:
        dictionary["telefono"] = telefono
    
    return dictionary








contact = create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787)
print(create_contact("Mario Rossi", email="mario.rossi@gmail.com", telefono=788787))
print(update_contact(contact, "Mario Rossi", telefono=123456789))


contact = create_contact("Laura Neri", email="laura.neri@domain.com")
print(create_contact("Laura Neri", email="laura.neri@domain.com"))
print(update_contact(contact, "Laura Neri", email="laura.new@domain.com", telefono=84736736))
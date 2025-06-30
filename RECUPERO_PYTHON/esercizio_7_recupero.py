class ContactManager: #definizione della classe ContactManager
    def __init__(self,contacts:dict[str,list[str]])->None: #definizione del costruttore
        self.contacts:dict[str,list[str]] = contacts


    #definizione del metodo create_contact per aggiungere un nuovo contatto con una lista di numeri, Solleva un errore se il contatto esiste già
    def create_contact(self,name:str, phone_numbers:list[str])->dict[str,list[str]]:

        if name not in self.contacts: #se il contatto non è nella dizionario contacts
            self.contacts[name] = phone_numbers #aggiungo il contatto al dizionario originale
        else:
            print("Errore: il contatto esiste già") #rilascio errore se il contatto è già presente nella lista
        
        return {name: phone_numbers} #ritorna un dizionario con solo il contatto aggiunto
    

    #metodo per aggiungere un numero di telefono ad un determinato contatto. Solleva un errore se il contatto non esiste o il numero esiste già
    def add_phone_number(self,contact_name:str,phone_number:str)->dict[str,list[str]]:

        if contact_name not in self.contacts:  #verifico se il nome è già presente nel dizionario contacts
            print("Errore: il contatto non esiste")
        if phone_number in self.contacts[contact_name]: #verifico se il numero di telefono è già presente nel dizionario contacts
            print("Errore: il numero esiste già")
        
        self.contacts[contact_name].append(phone_number)   #aggiungo il numero al dizionario originale
        return {contact_name: self.contacts[contact_name]}
    

        #metodo per rimuovere un numero di telefono. Solleva un errore se il contatto non esiste o il numero esiste non esiste
    def remove_phone_number(self, contact_name:str , phone_number:str)->dict[str,list[str]]:

        if contact_name not in self.contacts: #verifico se il nome è già presente nel dizionario contacts
            print("Errore: il contatto non esiste")
        if phone_number not in self.contacts[contact_name]: #verifico se il numero è già presente nel dizionario contacts
            print("Errore: il numero non esiste")

        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
        #metodo per modificare un contatto sostituendo un numero. Solleva un errore se il contatto non esisteo il numero da sostituire non esiste o il numero nuovo esiste già
    def update_phone_number(self, contact_name:str, old_phone_number:str, new_phone_number:str)->dict[str,list[str]]:

        if contact_name not in self.contacts: #verifico se il nome è già presente nel dizionario contacts
            print("Errore: il contatto non esiste")
        if old_phone_number not in self.contacts[contact_name]: #verifico se il numero è già presente nel dizionario contacts
            print("Errore: il numero non esiste")
        if new_phone_number in self.contacts[contact_name]: #verifico che il nuovo numero non sia già presente nel dizionario contacts
            print("Errore: il numero è già presente")
        
        self.contacts[contact_name].remove(old_phone_number) #rimuovo il precedente numero
        self.contacts[contact_name].append(new_phone_number) #aggiungo il nuovo numero
        return {contact_name: self.contacts[contact_name]}
    
    #metodo per mostra la lista contatti
    def list_contacts(self)->list[str]:
        return list(self.contacts.keys())
    

    #metodo per mostrare tutti i numeri di un determinato contatto
    def list_phone_numbers(self,contact_name:str)->list[str]:
        if contact_name not in self.contacts:
            print("Errore: il contatto non esiste")
        else:
            return self.contacts[contact_name]
        

    #metodo per cercare un contatto direttamente da un numero di telefono
    def search_contact_by_phone_number(self, phone_number:str)->list[str]:
        found_contacts = []

        for name,numbers in self.contacts.items(): #ciclo for per scomporre chiave e valore
            if phone_number in numbers:    #verifico se il numero è presente nel dizionario contacts
                found_contacts.append(name)
        if not found_contacts:   #se non abbiamo trovato contatti diamo un errore
            print("Nessun contatto trovato con questo numero di telefono")
        return found_contacts
    


if __name__ == "__main__":

    initial_contacts = {
    "Alice": ["111111111", "222222222"],
    "Bob": ["333333333"],
    "Carla": ["444444444", "555555555", "666666666"],
    "Davide": ["777777777"],
    "Elisa": ["888888888"],
    "Fabio": ["999999999"],
    "Gina": ["123123123", "321321321"],
    "Luca": ["456456456"],
    "Maria": ["789789789", "987987987"],
    "Paolo": ["654654654"]
}

    cm:ContactManager = ContactManager(initial_contacts)

    print("Contatti iniziali:")
    print(cm.list_contacts())
    print()

    
    print("Aggiungo contatto 'Sara':", cm.create_contact("Sara", ["111222333"]))
    
    print()

    
    print("Aggiungo contatto 'Alice' di nuovo:", cm.create_contact("Alice", ["000000000"]))
    print()


    print("Aggiungo numero a 'Bob':", cm.add_phone_number("Bob", "444555666"))
    print()


    print("Rimuovo numero da 'Carla':", cm.remove_phone_number("Carla", "555555555"))

    print()

    print("Aggiorno numero di 'Maria':", cm.update_phone_number("Maria", "789789789", "111999888"))

    print()


    print("Numeri di 'Gina':", cm.list_phone_numbers("Gina"))

    print()

    print("Contatti con numero '333333333':", cm.search_contact_by_phone_number("333333333"))
    print()

    print("Contatti con numero '000000000':", cm.search_contact_by_phone_number("000000000"))

    print()

            

                


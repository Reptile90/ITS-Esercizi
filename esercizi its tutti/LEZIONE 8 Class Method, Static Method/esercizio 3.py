class Book:
    def __init__(self, title:str, author:str, isbn:int):
        self.title = title 
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Titolo: {self.title}\nAutore: {self.author}\nIsbn: {self.isbn}"
    
    @classmethod
    def from_string(cls,book_string):
        parts = book_string.split(',')
        title = parts[0].strip()
        author = parts[1].strip()
        isbn = int(parts[2].strip())
        return cls(title, author, isbn)
    


class Member:
    def __init__(self, name:str, member_id:int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


    def borrow_books(self, book:Book) -> None:
        self.borrowed_books.append(book)

    def return_book(self,book:Book)->None:
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        books_info = ""
        if len(self.borrowed_books) == 0:
            books_info = "Nessun libro in prestito"
        else:
            for book in self.borrowed_books:
                books_info += str(book) + "\n"

        return f"Membro: {self.name} (ID: {self.member_id})\nLibri in prestito:\n{books_info.strip()}"
    
    @classmethod
    def from_string(cls, member_string: str):
        parts = member_string.split(',')
        name = parts[0].strip()
        member_id = int(parts[1].strip())
        return cls(name, member_id)
    
class Library:
    total_books = 0
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book:Book)->None:
        self.books.append(book)
        Library.total_books += 1


    def remove_book(self, book:Book)->None:
        if book in self.books:
            self.books.remove(book)
        Library.total_books -= 1

    def register_member(self, member:Member)->None:
        self.members.append(member)

    def lend_book(self, book: Book, member: Member) -> None:
        if book not in self.books:
            print("Libro non disponibile.")
            return

        if member not in self.members:
            print("Membro non registrato.")
            return

        member.borrow_books(book)
        self.books.remove(book)
        Library.total_books -= 1

    def __str__(self):
        result = "LIBRERIA\n\nLibri disponibili:\n"
        if len(self.books) == 0:
            result += "Nessun libro disponibile.\n"
        else:
            for book in self.books:
                result += str(book) + "\n---\n"

        result += "\nMembri registrati:\n"
        if len(self.members) == 0:
            result += "Nessun membro registrato.\n"
        else:
            for member in self.members:
                result += str(member) + "\n---\n"

        return result.strip()
    
    @classmethod
    def library_statistics(cls):
        print(f"Totale libri in biblioteca: {cls.total_books}")




library = Library()

book1 = Book.from_string("Il nome della rosa, Umberto Eco, 12345")
book2 = Book.from_string("1984, George Orwell, 54321")

member1 = Member.from_string("Alice Rossi, 1")
member2 = Member.from_string("Luca Bianchi, 2")

library.register_member(member1)
library.register_member(member2)


library.add_book(book1)
library.add_book(book2)


print(">>> Stato della libreria prima dei prestiti:\n")
print(library)
print("\n")
Library.library_statistics()
print("\n")


library.lend_book(book1, member1)


print(">>> Stato della libreria dopo i prestiti:\n")
print(library)
print("\n")
Library.library_statistics()

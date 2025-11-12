class Book:
    def __init__(self,book_id:str, title:str,author:str,is_borrewed:bool=False):
        
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrewed
        
    def borrow(self)->None:
        if self.is_borrowed == False:
            self.is_borrowed = True
    
    def return_book(self)->None:
        if self.is_borrowed == True:
            self.is_borrowed =False
            
class Member:
    
    def __init__(self, member_id:str, name:str):
        
        self.member_id = member_id
        self.name = name
        self.borrowed_books:list[Book]
        
    def borrow_book(self,book:Book)->None:
        if book not in self.borrowed_books:
            if book.is_borrowed:
                self.borrowed_books.append(book)
            else:
                print(f"Il libro {book.title} non è stato noleggiato")
        else:
            print("Il libro non è stato noleggiato")
                  
            
        
        
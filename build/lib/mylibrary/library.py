class Library():
    def __init__(self,library=None):
        if library is None:
            self.library={}
        else:
            self.library=library
     
    def add_book(self,title,author):
        self.library[title] = author
       
    def remove_book(self,title):
        if title in self.library:
            print(f"book {title} written by {self.library[title]} deleted")
            del self.library[title]
        else:
            print(f"The book {title} not found")
        
    def search_book(self,title):
        if title in self.library:
            return(self.library[title])
        else:
            print(f"The book {title} not found")
    
    def show_books(self):
        return self.library.items()
    
dehgan=Library()

dehgan.add_book("iran","zahra")

dehgan.add_book("Arak","Ali")
print(dehgan.show_books())
print(dehgan.search_book("Arak"))
dehgan.remove_book("Arak")
print(dehgan.show_books())


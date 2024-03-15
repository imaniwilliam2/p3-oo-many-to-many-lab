class Author:
     
    all = []
    
    def __init__(self, name):
        self.name = name

        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        contract =  Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total



class Book:

    all = []
    
    def __init__(self, title):
        self.title = title

        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author_param):
        if not isinstance(author_param, Author):
            raise Exception("Author must be an instance of the Author class.")
        self._author = author_param

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book_param):
        if not isinstance(book_param, Book):
            raise Exception("Book must be an instance of the Book class.")
        self._book = book_param

    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date_param):
        if not isinstance(date_param, str):
            raise Exception("Date must be a string.")
        self._date = date_param

    @property 
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties_param):
        if not isinstance(royalties_param, int):
            raise Exception("Royalties must be a number.")
        self._royalties = royalties_param


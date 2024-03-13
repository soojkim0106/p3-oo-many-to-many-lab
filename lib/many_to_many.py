class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return list({contract.book for contract in self.contracts()})
   
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        
        contracts_list = []
        
        for contract in Contract.all:
            if contract.book == self:
                contracts_list.append(contract)
                
        return contracts_list
    
    def authors(self):
        
        return [contract.author for contract in self.contracts()]

class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception('author is not instance of Author class')
        self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception('book is not instance of Book class')
        self._book = book
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date,str):
            raise Exception('date is not a string')
        self._date = date
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception('royalties is not a int')
        self._royalties = royalties
        
    @classmethod
    def contracts_by_date(cls,date):
        # return [contract for contract in cls.all if contract.date == date]
        
        contract_list = []
        
        for contract in cls.all:
            if contract.date == date:
                contract_list.append(contract)
                
        return contract_list
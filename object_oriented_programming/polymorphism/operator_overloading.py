class book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):                   #this is a spcl builtin method allows us to
        return book(self.pages + other.pages)   #add the values of two class type like b1 and b2
                                                # another thing to note here is the output is converted to
                                                #book type(book is class here) because wen return of b1+b2 which
                                                #will be a book type is added with b3 which is another book type
                                                #sum of book(b1+b3) + b3(already a book type) will be a book type
                                                # to convert them into str builtin def__str__ is used
    def __str__(self):
        return str(self.pages)
b1=book(100)
b2=book(200)
b3=book(300)
print(b1+b2+b3)
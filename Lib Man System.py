class Book:
    def __init__(self):
        self.BookID=""
        self.Title=""
        self.AuthorID=""
        self.Publisher=""
        self.YoP=""
        self.Availability=""
        self.Description=""
        self.AuthorInfo=[]
    def addBook(self):
        self.BookID = input("Enter book ID:")
        self.Title = input("Enter the title:")
        self.AuthorID = input("Enter the author:")
        self.Publisher= input("Enter the publisher:")
        self.YoP= input("Enter the year of publication:")
        self.Description= input("Please enter the book Description")
        self.Availability="Available"
    def editBook(self):
        self.BookID = input("Enter book ID:")
        self.Title = input("Enter the new title:")
        self.AuthorID = input("Enter the new author:")
        self.Publisher = input("Enter the new publisher:")
        self.YoP = input("Enter the new year of publication:")
        self.Description = input("Please enter the new book description")
    def deleteBook(self):

    def displayBook(self):
        print("Book ID:", self.BookID)
        print("Title:", self.Title)
        print("Author:", self.AuthorID)
        print("Publisher:", self.Publisher)
        print("Year of Publication:", self.YoP)
        print("Description:", self.Description)
        print(self.Availability, "to borrow")
    def borrowBook(self):
        self.Availability="Unavailable"
    def returnBook(self):
        self.Availability="Available"
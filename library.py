from database import Database
from datetime import datetime


class Library:

    def __init__(self):
        self.db = Database()

    def add_book(self):

        book_id = input("Book ID : ")
        title = input("Title : ")
        author = input("Author : ")
        quantity = int(input("Quantity : "))

        self.db.execute(
            "INSERT INTO books VALUES(?,?,?,?,?)",
            (book_id, title, author, quantity, quantity)
        )

        print("Book Added Successfully.")

    def display_books(self):

        books = self.db.fetchall("SELECT * FROM books")

        print("\nLibrary Books\n")

        for book in books:
            print("--------------------------------")
            print("Book ID :", book[0])
            print("Title :", book[1])
            print("Author :", book[2])
            print("Quantity :", book[3])
            print("Available :", book[4])

    def search_book(self):

        keyword = input("Enter Title : ")

        books = self.db.fetchall(
            "SELECT * FROM books WHERE title LIKE ?",
            ('%' + keyword + '%',)
        )

        if not books:
            print("Book Not Found")
            return

        for book in books:
            print(book)

    def issue_book(self):

        book_id = input("Book ID : ")

        books = self.db.fetchall(
            "SELECT available FROM books WHERE book_id=?",
            (book_id,)
        )

        if not books:
            print("Book Not Found")
            return

        available = books[0][0]

        if available == 0:
            print("Book Out of Stock")
            return

        self.db.execute(
            "UPDATE books SET available=available-1 WHERE book_id=?",
            (book_id,)
        )

        print("Book Issued Successfully")

    def return_book(self):

        book_id = input("Book ID : ")

        self.db.execute(
            "UPDATE books SET available=available+1 WHERE book_id=?",
            (book_id,)
        )

        print("Book Returned Successfully")

    def delete_book(self):

        book_id = input("Book ID : ")

        self.db.execute(
            "DELETE FROM books WHERE book_id=?",
            (book_id,)
        )

        print("Book Deleted Successfully")

    def calculate_fine(self):

        issue = input("Issue Date (YYYY-MM-DD): ")
        ret = input("Return Date (YYYY-MM-DD): ")

        issue_date = datetime.strptime(issue, "%Y-%m-%d")
        return_date = datetime.strptime(ret, "%Y-%m-%d")

        days = (return_date - issue_date).days

        if days <= 7:
            fine = 0
        else:
            fine = (days - 7) * 5

        print("Fine =", fine)
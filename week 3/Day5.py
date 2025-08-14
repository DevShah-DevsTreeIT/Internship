    # Library Management System:- Build an OOP-based system to manage books, members, and borrowing
"""
class Library:
    def availablebooks,add/remove books,
        attribute :book - title, author ,publish year 
class student: 
    def borrow,Timeperiod,borrowed_books,

"""


class Book:

    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.book_id}: '{self.title}' by {self.author} ({self.year}) - {status}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        borrowed = ', '.join(book.title for book in self.borrowed_books) or "None"
        return f"{self.member_id}: {self.name} - Borrowed Books: {borrowed}"


class Library:
    # print("Welcome the `")
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added.")

    def register_member(self, member):
        self.members[member.member_id] = member
        print(f"Member '{member.name}' registered.")

    def borrow_book(self, member_id, book_id):
        if member_id not in self.members:
            print("❌ Member not found.")
            return
        if book_id not in self.books:
            print("❌ Book not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_borrowed:
            print("❌ Book already borrowed.")
        else:
            book.is_borrowed = True
            member.borrowed_books.append(book)
            print(f"✅ {member.name} has borrowed '{book.title}'.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            print("❌ Invalid member or book.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"✅ {member.name} has returned '{book.title}'.")
        else:
            print("❌ This book was not borrowed by this member.")

    def list_books(self):
        if not self.books:
            print("📚 No books in the library.")
        for book in self.books.values():
            print(book)

    def list_members(self):
        if not self.members:
            print("👤 No members registered.")
        for member in self.members.values():
            print(member)


# ==== Menu-driven Interface ====

def main():
    library = Library()

    while True:
        print("\n################# RK Library Management System 📚 #################")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List All Books")
        print("6. List All Members")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Year of Publish: ")
            book = Book(book_id, title, author, year)
            library.add_book(book)

        elif choice == '2':
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            member = Member(member_id, name)
            library.register_member(member)

        elif choice == '3':
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            library.borrow_book(member_id, book_id)

        elif choice == '4':
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            library.return_book(member_id, book_id)

        elif choice == '5':
            print("\n📚 Books in Library:")
            library.list_books()

        elif choice == '6':
            print("\n👤 Registered Members:")
            library.list_members()

        elif choice == '7':
            print("Exiting the RK Library 📚 System, bye!")
            break

        else:
            print("Invalid choice.` Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
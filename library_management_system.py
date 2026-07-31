"""
Library Management System
A simple command-line app to manage books in a library:
add, view, search, issue, return, and delete books.

Data is saved to books.json so your library persists between runs.
"""

import json
import os

DATA_FILE = "books.json"


class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    def display(self):
        print("-" * 40)
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Issued" if self.issued else "Available")

    def to_dict(self):
        """Convert Book object to a dictionary so it can be saved as JSON."""
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued": self.issued,
        }

    @staticmethod
    def from_dict(data):
        """Rebuild a Book object from a dictionary loaded from JSON."""
        return Book(data["book_id"], data["title"], data["author"], data["issued"])


books = []


def load_books():
    """Load saved books from books.json, if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return [Book.from_dict(b) for b in data]
            except json.JSONDecodeError:
                print("Warning: books.json was corrupted, starting with an empty library.")
                return []
    return []


def save_books():
    """Save the current list of books to books.json."""
    with open(DATA_FILE, "w") as f:
        json.dump([book.to_dict() for book in books], f, indent=4)


def find_book(book_id):
    """Return the Book object matching book_id, or None if not found."""
    for book in books:
        if book.book_id == book_id:
            return book
    return None


def get_book_id_input():
    """Prompt for a Book ID and validate it's an integer."""
    try:
        return int(input("Enter your Book ID: "))
    except ValueError:
        print("Invalid Input!")
        return None


def add_book():
    try:
        book_id = int(input("Enter Book ID: "))
    except ValueError:
        print("Invalid Input!")
        return

    if find_book(book_id):
        print("A book with this ID already exists.")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    if not title or not author:
        print("Title and author cannot be empty.")
        return

    books.append(Book(book_id, title, author))
    save_books()
    print("Book Added successfully!")


def view_books():
    if not books:
        print("No books available.")
        return
    for book in books:
        book.display()


def search_book():
    book_id = get_book_id_input()
    if book_id is None:
        return
    book = find_book(book_id)
    if book:
        book.display()
    else:
        print("Book not found.")


def issue_book():
    book_id = get_book_id_input()
    if book_id is None:
        return
    book = find_book(book_id)
    if not book:
        print("Book not found.")
        return
    if book.issued:
        print("Book Already Issued")
    else:
        book.issued = True
        save_books()
        print("Book issued successfully!")


def return_book():
    book_id = get_book_id_input()
    if book_id is None:
        return
    book = find_book(book_id)
    if not book:
        print("Book not found.")
        return
    if book.issued:
        book.issued = False
        save_books()
        print("Book returned successfully!")
    else:
        print("Book was not issued.")


def delete_book():
    book_id = get_book_id_input()
    if book_id is None:
        return
    book = find_book(book_id)
    if not book:
        print("Book not found.")
        return
    books.remove(book)
    save_books()
    print("Book deleted successfully!")


def main():
    global books
    books = load_books()

    while True:
        print("\n ========= LIBRARY MANAGEMENT SYSTEM =========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Thank you!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

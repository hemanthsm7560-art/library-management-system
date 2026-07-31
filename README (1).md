# 📚 Library Management System

A command-line Library Management System built in Python. Manage books — add, view, search, issue, return, and delete — with data automatically saved between sessions.

## Features

- **Add Book** — Add a new book with a unique ID, title, and author
- **View Books** — List all books currently in the library, with issue status
- **Search Book** — Find a book by its ID
- **Issue Book** — Mark a book as issued to a borrower
- **Return Book** — Mark an issued book as returned
- **Delete Book** — Remove a book from the library
- **Persistent Storage** — All data is saved to `books.json`, so your library isn't wiped when you close the program

## Tech Stack

- Python 3
- Built-in `json` module for data persistence
- Object-Oriented Programming (`Book` class)

## How to Run

```bash
python library_management_system.py
```

You'll see a menu-driven interface:

```
 ========= LIBRARY MANAGEMENT SYSTEM =========
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
Enter your choice:
```

## Project Structure

```
library-management-system/
├── library_management_system.py   # Main application code
├── books.json                     # Auto-generated data file (created on first run)
└── README.md
```

## What I Learned

- Structuring a project with Object-Oriented Programming
- Reading and writing structured data using JSON for persistence
- Input validation and error handling with `try/except`
- Refactoring repeated code into reusable helper functions

## Possible Future Improvements

- Add due dates and fine calculation for late returns
- Track which borrower issued which book
- Add a search-by-title or search-by-author option
- Build a simple GUI using Tkinter, or a web version with Flask/Streamlit

---
*Built as part of my Python learning journey.*

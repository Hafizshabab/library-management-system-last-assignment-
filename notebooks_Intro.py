{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "class Book:\n    def _init_(self, title, author, isbn, total_copies):\n        self.title = title\n        self.author = author\n        self.isbn = isbn\n        self.total_copies = total_copies\n        self.available_copies = total_copies\n\nclass Patron:\n    def _init_(self, name, patron_id):\n        self.name = name\n        self.patron_id = patron_id\n        self.books_borrowed = []\n\nclass Library:\n    def _init_(self):\n        self.books = []\n        self.patrons = []\n\n    def add_book(self, book):\n        self.books.append(book)\n\n    def add_patron(self, patron):\n        self.patrons.append(patron)\n\n    def borrow_book(self, patron, book):\n        if book in self.books and book.available_copies > 0:\n            if book not in patron.books_borrowed:\n                patron.books_borrowed.append(book)\n                book.available_copies -= 1\n                print(f\"{patron.name} has successfully borrowed {book.title}.\")\n            else:\n                print(f\"{patron.name} already borrowed {book.title}.\")\n        else:\n            print(\"Book is not available for borrowing.\")\n\n    def return_book(self, patron, book):\n        if book in patron.books_borrowed:\n            patron.books_borrowed.remove(book)\n            book.available_copies += 1\n            print(f\"{patron.name} has successfully returned {book.title}.\")\n        else:\n            print(f\"{patron.name} did not borrow {book.title}.\")\n\nclass Catalog:\n    @staticmethod\n    def display_books(library):\n        for book in library.books:\n            print(f\"{book.title} by {book.author} (ISBN: {book.isbn})\")\n\n    @staticmethod\n    def display_patrons(library):\n        for patron in library.patrons:\n            print(f\"{patron.name} (Patron ID: {patron.patron_id})\")\n\n# Example usage\nif _name_ == \"_main_\":\n    library = Library()\n\n    book1 = Book(\"Book 1\", \"Author 1\", \"ISBN001\", 5)\n    book2 = Book(\"Book 2\", \"Author 2\", \"ISBN002\", 3)\n    library.add_book(book1)\n    library.add_book(book2)\n\n    patron1 = Patron(\"Patron 1\", \"P001\")\n    patron2 = Patron(\"Patron 2\", \"P002\")\n    library.add_patron(patron1)\n    library.add_patron(patron2)\n\n    library.borrow_book(patron1, book1)\n    library.borrow_book(patron2, book1)\n    library.return_book(patron1, book1)\n\n    Catalog.display_books(library)\n    Catalog.display_patrons(library)",
      "metadata": {
        "trusted": true
      },
      "execution_count": null,
      "outputs": [],
      "id": "934bef2b-b1fa-4588-b848-98ed826515d8"
    },
    {
      "cell_type": "code",
      "source": "",
      "metadata": {},
      "execution_count": null,
      "outputs": [],
      "id": "15db2326-f030-4402-9565-9a604ffab3f6"
    }
  ]
}
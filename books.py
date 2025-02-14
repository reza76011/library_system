def add_book(title, author, subject, year):
    books = load_data("books.dat")
    books[title] = [author, subject, year]
    save_data("books.dat", books)

def search_book(title):
    books = load_data("books.dat")
    print(books.get(title, "Book not found!"))
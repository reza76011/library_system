def borrow_book(user_id, title):
    borrows = load_data("borrows.dat")
    borrows[user_id] = title
    save_data("borrows.dat", borrows)

def show_all_info():
    print("Users:", load_data("users.dat"))
    print("Books:", load_data("books.dat"))
    print("Borrows:", load_data("borrows.dat"))

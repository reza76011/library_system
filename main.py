from users import add_user
from books import add_book, search_book
from borrows import borrow_book, show_all_info

def main():
    while True:
        print("1- Add User\n2- Add Book\n3- Search\n4- Borrow\n5- Show All\n0- Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            add_user(
                input("Name: "), input("Family: "), input("Father's Name: "),
                input("National Code: "), input("Birthday: ")
            )
        elif ch == "2":
            add_book(input("Title: "), input("Author: "), input("Subject: "), input("Year: "))
        elif ch == "3":
            search_book(input("Title: "))
        elif ch == "4":
            borrow_book(input("User ID: "), input("Title: "))
        elif ch == "5":
            show_all_info()
        elif ch == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        else:
            return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        else:
            return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("\n--Book no longer exist--\n")
        else:
            print("List of existing books :")
            for i, book in enumerate(self.books):
                status = "Available" if not book.is_borrowed else "Borrow"
                print(f"{i+1}. {book.title} oleh {book.author} - {status}")

def main():
    library = Library()
    admin_mode = False

    while True:
        if not admin_mode:
            print("\n--Welcome to the Libarary--")
            print("1. Login as Admin")
            print("2. Login as User")
            print("3. Exit")
            choice = input("choose: ")

            if choice == '1':
                admin_mode = True
                continue
            elif choice == '2':
                user_menu(library)
            elif choice == '3':
                break
            else:
                print("Your option doesnt exist.")
        else:
            print("\nMenu Admin:")
            print("1. Add book")
            print("2. Back to menu")
            choice = input("choose: ")

            if choice == '1':
                title = input("Add book title: ")
                author = input("Add the creator name: ")
                library.add_book(title, author)
                print("Book succsessfully update.")
            elif choice == '2':
                admin_mode = False
            else:
                print("your option doesnt exist.")

def user_menu(library):
    while True:
        print("\nMenu User:")
        print("1. borrow a book")
        print("2. return a book")
        print("3. book list")
        print("4. back to menu")
        choice = input("Choose: ")

        if choice == '1':
            library.display_books()
            book_index = int(input("choose number of book to borrow: ")) - 1
            if 0 <= book_index < len(library.books):
                if library.books[book_index].borrow():
                    print("book succsessfully borrowed.")
                else:
                    print("book already borrow.")
            else:
                print("number of book doesnt exist.")
        elif choice == '2':
            library.display_books()
            book_index = int(input("choose number of book for returnig: ")) - 1
            if 0 <= book_index < len(library.books):
                if library.books[book_index].return_book():
                    print("Book already returned.")
                else:
                    print(" The Book not borrowed yet.")
            else:
                print("The number of book doesnt exist.")
        elif choice == '3':
            library.display_books()
        elif choice == '4':
            break
        else:
            print("There is no option.")

if __name__ == "__main__":
    main()

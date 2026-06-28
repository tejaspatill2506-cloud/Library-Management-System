from library import Library

library = Library()

while True:

    print("\n========== Library Management ==========")

    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Calculate Fine")
    print("8. Exit")

    choice = input("Enter Choice : ")

    try:

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.delete_book()

        elif choice == "7":
            library.calculate_fine()

        elif choice == "8":
            library.db.close()
            print("Thank You")
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        print("Error :", e)
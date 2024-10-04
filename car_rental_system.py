def menu():
    print("\nCar Rental System Menu:",
            "1. Reserve a car",
            "2. Show all reservations",
            "3. Remove a reservation",
            "4. Exit",
            sep="\n")


if __name__ == '__main__':
    while True:
        menu()
        choice = input("Please choose an option: ")
        if choice == '1':
            print("\nCreated a reservation.")
        elif choice == '2':
            print("\nShowing reservations:")
        elif choice == '3':
            print("\nRemoved a reservation.")
        elif choice == '4':
            print("\nClosing the application.")
            break
        else:
            print("Invalid option, please try again.")
            continue

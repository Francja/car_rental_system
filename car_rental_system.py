import datetime


# Car class with the car type and number of cars available:
class Car:
    def __init__(self, car_type, count):
        self.car_type = car_type
        self.count = count


# Reservation class to store reservation details
class Reservation:
    _id_num = 1

    def __init__(self, car_type, start_date, number_of_days):
        self.car_type = car_type
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M")
        self.number_of_days = number_of_days
        self.reservation_id = Reservation._id_num
        Reservation._id_num += 1


# CarRentalSystem class to manage cars and reservations
class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.reservations = []

    def reserve_car(self):
        print("\nCar reserved")

    def show_reservations(self):
        print("\nShowing reservations")

    def remove_reservation(self):
        print("\nRemoved reservation")


def menu():
    print("\nCar Rental System Menu:",
            "1. Reserve a car",
            "2. Show all reservations",
            "3. Remove a reservation",
            "4. Exit",
            sep="\n")


if __name__ == '__main__':

    crs = CarRentalSystem()

    while True:
        menu()
        choice = input("\nPlease choose an option: ")
        if choice == '1':
            crs.reserve_car()
        elif choice == '2':
            crs.show_reservations()
        elif choice == '3':
            crs.remove_reservation()
        elif choice == '4':
            print("\nClosing the application.")
            break
        else:
            print("Invalid option, please try again.")
            continue

import datetime


# Car class with the car type and number of cars available:
class Car:
    def __init__(self, car_type, count):
        self.car_type = car_type
        self.count = count

    def __str__(self):
        return f"{self.car_type} (Count: {self.count})"


# Reservation class to store reservation details
class Reservation:
    _id_num = 1

    def __init__(self, car_type, start_date, number_of_days):
        self.car_type = car_type
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M")
        self.number_of_days = number_of_days
        self.reservation_id = Reservation._id_num
        Reservation._id_num += 1

    def __str__(self):
        return f"ID {self.reservation_id}: {self.car_type} from {self.start_date} for {self.number_of_days} days."

# CarRentalSystem class to manage cars and reservations
class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.reservations = []

    def add_cars(self, car_type, count):
        self.cars.append(Car(car_type, count))

    def show_cars(self):
        for car in self.cars:
            print(car)

    def reserve_car(self, car_type, start_date, number_of_days):
        for car in self.cars:
            if car.car_type == car_type and car.count > 0:
                new_reservation = Reservation(car_type,start_date,number_of_days)
                self.reservations.append(new_reservation)
                car.count -= 1
                return Reservation


    def show_reservations(self):
        for reservation in self.reservations:
            print(reservation)

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
    crs.add_cars("Sedan", 2)
    crs.add_cars("SUV", 1)
    crs.add_cars("Van", 3)
    crs.show_cars()

    while True:
        menu()
        choice = input("\nPlease choose an option: ")
        if choice == '1':
            car_type = input("Enter car type: ")
            start_date = input("Enter start date (YYYY-MM-DD HH:MM): ")
            number_of_days = int(input("Enter number of days: "))
            crs.reserve_car(car_type, start_date, number_of_days)
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

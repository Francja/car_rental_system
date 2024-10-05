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
        self.start_date = start_date
        self.number_of_days = number_of_days
        self.end_date = self.start_date + datetime.timedelta(days=number_of_days)
        self.reservation_id = Reservation._id_num
        Reservation._id_num += 1

    def __str__(self):
        return f"ID {self.reservation_id}: {self.car_type} from {self.start_date} to {self.end_date} "


# CarRentalSystem class to manage cars and reservations
class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.reservations = []

    def add_cars(self, car_type, count):
        self.cars.append(Car(car_type, count))

    def show_cars(self):
        print("\nAvailable cars:")
        for car in self.cars:
            print(car)

    def reserve_car(self, car_type, start_date, number_of_days):
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M")
        number_of_days = int(number_of_days)
        if not self.is_car_available(car_type, start_date, number_of_days):
            print("\nNo cars available for this type and date")
        else:
            new_reservation = Reservation(car_type, start_date, number_of_days)
            self.reservations.append(new_reservation)
            print(f"\nNew reservation: {new_reservation}")

    def is_car_available(self, car_type, start_date, number_of_days):

        end_date = start_date + datetime.timedelta(days=number_of_days)

        # Find total cars available for the type requested
        total_cars_available = 0
        for car in self.cars:
            if car.car_type == car_type:
                total_cars_available = car.count

        # Create a list of events (start of reservation: +1, end of reservation: -1)
        events = []
        for reservation in self.reservations:
            if reservation.car_type == car_type:
                # Start of reservation
                events.append((reservation.start_date, 1))
                # End of reservation
                events.append((reservation.end_date, -1))

        # Add currently made reservation to the list of events:
        events.append((start_date, 1))
        events.append((end_date, -1))

        # Sort events by time, then by value if they collide
        # so cars can end/begin reservation at the same time
        events.sort(key=lambda element: (element[0], element[1]))

        # Sweep through already existing and new reservation and check
        #  if it exceeds the number of cars available at any moment
        active_reservations = 0
        for time, value in events:
            active_reservations += value
            if active_reservations > total_cars_available:
                return False
        return True

    def show_reservations(self):
        for reservation in self.reservations:
            print(reservation)

    def remove_reservation(self, reservation_id):
        reservation_id = int(reservation_id)
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                self.reservations.remove(reservation)
        print(f"\nReservation {reservation_id} removed.")


def menu():
    print("\nCar Rental System Menu:",
            "1. Reserve a car",
            "2. Show cars available",
            "3. Show all reservations",
            "4. Remove a reservation",
            "5. Exit",
            sep="\n")


if __name__ == '__main__':


    crs = CarRentalSystem()
    crs.add_cars("Sedan", 1)
    crs.add_cars("SUV", 2)
    crs.add_cars("Van", 3)

    # basic unit testing for now
    crs.show_cars()
    crs.reserve_car("SUV", "2023-03-01 13:00", 5)
    crs.reserve_car("Sedan", "2023-03-01 13:00", 5)
    crs.reserve_car("Sedan", "2023-03-01 13:00", 5)
    crs.reserve_car("Ford Focus", "2023-03-01 13:00", 5)
    crs.reserve_car("SUV", "2023-03-06 13:00", 5)
    crs.reserve_car("SUV", "2023-03-03 12:00", 5)
    crs.reserve_car("SUV", "2023-03-03 12:00", 5)
    crs.show_reservations()
    crs.remove_reservation(1)
    crs.reserve_car("SUV", "2023-03-03 12:00", 1)
    crs.show_reservations()

    while True:
        menu()
        choice = input("\nPlease choose an option: ")
        if choice == '1':
            car_type = input("Enter car type: ")
            start_date = input("Enter start date (YYYY-MM-DD HH:MM): ")
            number_of_days = input("Enter number of days: ")
            crs.reserve_car(car_type, start_date, number_of_days)
        elif choice == '2':
            crs.show_cars()
        elif choice == '3':
            crs.show_reservations()
        elif choice == '4':
            reservation_id = input("Enter reservation ID to be removed: ")
            crs.remove_reservation(reservation_id)
        elif choice == '5':
            print("\nClosing the application.")
            break
        else:
            print("Invalid option, please try again.")
            continue

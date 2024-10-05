import datetime
from car_rental_system import CarRentalSystem, Car, Reservation


def test_car_addition():
    crs = CarRentalSystem()
    crs.add_cars("Sedan", 1)
    crs.add_cars("SUV", 2)

    assert len(crs.cars) == 2, "Test Failed: Number of types of cars should be 2"
    assert crs.cars[0].car_type == "Sedan", "Test Failed: First car type should be Sedan"
    assert crs.cars[0].count == 1, "Test Failed: Sedan count should be 1"

    crs.add_cars("Sedan", 2)

    assert crs.cars[0].count == 3, "Test Failed: Sedan count should be 2"

def test_car_addition_errors():
    crs = CarRentalSystem()
    crs.add_cars("Sedan", 1)
    crs.add_cars("Truck", 1) # <- fail
    crs.add_cars("Bus", 1) # <- fail
    crs.add_cars("Sedan", "sdgs") # <- fail
    crs.add_cars("Sedan", -123) # <- fail
    assert len(crs.cars) == 1, "Test Failed: Number of types of cars should be 1"

def test_reserving_cars():
    crs = CarRentalSystem()
    crs.add_cars("SUV", 2)
    crs.reserve_car("SUV", "2023-03-01 10:00", 3)
    crs.reserve_car("SUV", "2023-03-04 10:00", 2)
    crs.reserve_car("SUV", "2023-03-01 10:00", 5)

    assert len(crs.reservations) == 3, "Test Failed: Reservation count should be 3"

def test_reserving_cars_errors():
    crs = CarRentalSystem()
    crs.add_cars("SUV", 1)
    crs.reserve_car("SUV", "2023-03-04 10:00", 2)
    crs.reserve_car("Truck", "2023-03-01 10:00", 3) # <- fail
    crs.reserve_car("SUV", "20-03-04 10:00", 2) # <- fail
    crs.reserve_car("SUV", "2023-03-01 10:00", "five days") # <- fail
    crs.reserve_car("SUV", "2023-03-01 10:00", 0) # <- fail

    assert len(crs.reservations) == 1, "Test Failed: Reservation count should be 1"

def test_reserve_car_collision():
    crs = CarRentalSystem()
    crs.add_cars("SUV", 2)
    crs.reserve_car("SUV", "2023-03-01 10:00", 5)
    crs.reserve_car("SUV", "2023-03-01 10:00", 12)
    crs.reserve_car("SUV", "2023-03-06 10:00", 1)
    crs.reserve_car("SUV", "2023-03-07 10:00", 1)
    crs.reserve_car("SUV", "2023-03-08 09:50", 1) # <- collision
    crs.reserve_car("SUV", "2023-03-03 12:00", 5) # <- collision

    assert len(crs.reservations) == 4, "Test Failed: Reservation count should be 4"


def test_remove_reservations():
    crs = CarRentalSystem()
    crs.add_cars("SUV", 1)
    crs.reserve_car("SUV", "2023-03-01 10:00", 5)
    crs.remove_reservation(2) # <- fail
    crs.remove_reservation(-22) # <- fail
    crs.remove_reservation("sds") # <- fail
    crs.remove_reservation(1)
    assert len(crs.reservations) == 0, "Test Failed: Reservation count should be 0"


def test_show_cars():
    crs = CarRentalSystem()
    crs.add_cars("SUV", 1)
    crs.show_cars()


def test_show_reservations():
    crs = CarRentalSystem()
    crs.add_cars("SUV", 1)
    crs.reserve_car("SUV", "2023-03-01 10:00", 5)
    crs.show_reservations()


if __name__ == "__main__":
    test_car_addition()
    test_car_addition_errors()
    test_reserving_cars()
    test_reserving_cars_errors()
    test_reserve_car_collision()
    test_remove_reservations()
    test_show_cars()
    test_show_reservations()

    print("\nAll tests passed")

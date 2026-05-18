from src.models.passenger_car import PassengerCar
from src.models.rental import Rental
from src.models.rental_company import RentalCompany
from src.models.truck import Truck


def create_initial_rental_company():
    rental_company = RentalCompany("8ence Car Rentals")

    car_1 = PassengerCar("PHY-060", "Opel Corsa D", 120000, 5)
    car_2 = PassengerCar("AA-IE-323", "Suzuki S-Cross", 175000, 5)
    truck_1 = Truck("TRX-909", "Ford Transit", 145000, 3000)

    rental_company.add_vehicle(car_1)
    rental_company.add_vehicle(car_2)
    rental_company.add_vehicle(truck_1)

    rental_1 = Rental(car_1, "2026-05-20", "Kovács János")
    rental_2 = Rental(car_2, "2026-05-20", "Kiss István Béla")
    rental_3 = Rental(truck_1, "2026_05_22", "Kolompár Dezső")
    rental_4 = Rental(car_1, "2026-06-01", "Horváth Sára")

    rental_company.add_rental(rental_1)
    rental_company.add_rental(rental_2)
    rental_company.add_rental(rental_3)
    rental_company.add_rental(rental_4)

    return rental_company

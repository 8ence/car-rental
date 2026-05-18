from src.models.rental_company import RentalCompany
from src.models.rental import Rental
from src.models.passenger_car import PassengerCar
from src.models.truck import Truck


def main():
    rental_company = RentalCompany("Benyesz Autókölcsönző")

    passenger_car = PassengerCar("PHY-060", "Opel Corsa", 120000, 5)
    truck = Truck("AA-GG-010", "Ford Transit", 250000, 3000)

    rental_company.add_vehicle(passenger_car)
    rental_company.add_vehicle(truck)

    rental = Rental(passenger_car, "2026-05-20", "Teszt Elek")
    rental_company.add_rental(rental)

    print(rental_company)

    print("\nAutók: ")
    for passenger_car in rental_company.get_vehicles():
        print(passenger_car)

    print("\nBérlések: ")
    for rental in rental_company.get_rentals():
        print(rental)

if __name__ == "__main__":
    main()
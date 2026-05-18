from src.models.passenger_car import PassengerCar
from src.models.rental_company import RentalCompany
from src.services.rental_service import RentalService


def main():
    rental_company = RentalCompany("Benyesz Autókölcsönző")

    car = PassengerCar("PHY-060", "Opeal Corsa", 120000, 5)

    rental_company.add_vehicle(car)

    rental_service = RentalService(rental_company)

    try:

        price = rental_service.rent_vehicle(car, "2026-05-20", "John Don")

        print(f"Successfull rental! Price: {price} Ft")

        message = rental_service.cancel_rental(car, "2026-05-20")
        print(message)

        message = rental_service.cancel_rental(car, "2026-05-20")
        print(message)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()

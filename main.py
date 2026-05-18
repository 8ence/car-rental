from src.data import create_initial_rental_company
from src.services.rental_service import RentalService


def main():
    rental_company = create_initial_rental_company()
    rental_service = RentalService(rental_company)

    print(rental_company)

    print("\nInitial rentals:")
    for rental in rental_service.list_rentals():
        print(rental)


if __name__ == "__main__":
    main()
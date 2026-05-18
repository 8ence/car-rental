from src.data import create_initial_rental_company
from src.services.rental_service import RentalService
from src.ui.console_ui import ConsoleUi


def main():
    rental_company = create_initial_rental_company()
    rental_service = RentalService(rental_company)

    console_ui = ConsoleUi(rental_service, rental_company)
    console_ui.start()


if __name__ == "__main__":
    main()
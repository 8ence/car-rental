from datetime import datetime

from src.models.rental import Rental


class RentalService:

    def __init__(self, rental_company):
        self.__rental_company = rental_company

    def rent_vehicle(self, vehicle, date, renter):

        self.__validate_date(date)
        for rental in self.__rental_company.get_rentals():

            if (
                    rental.get_vehicle().get_registration_number() == vehicle.get_registration_number()
                    and rental.get_date() == date
            ):
                raise Exception("Vehicle is already rented for this date!")

        new_rental = Rental(vehicle, date, renter)

        self.__rental_company.add_rental(new_rental)

        return vehicle.get_daily_price()

    def cancel_rental(self, vehicle, date):

        self.__validate_date(date)
        for rental in self.__rental_company.get_rentals():

            if (
                    rental.get_vehicle().get_registration_number() == vehicle.get_registration_number()
                    and rental.get_date() == date
            ):
                self.__rental_company.get_rentals().remove(rental)
                return "Rental cancelled successfully!"

        raise Exception("Rental not found!")

    def list_rentals(self):
        rentals = self.__rental_company.get_rentals()

        if len(rentals) == 0:
            raise Exception("Rental not found!")

        return rentals

    def __validate_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise Exception("Invalid date format! Use YYYY-MM-DD.")
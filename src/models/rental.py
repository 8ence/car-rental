class Rental:
    def __init__(self, vehicle, date, renter):
        self.__vehicle = vehicle
        self.__date = date
        self.__renter = renter

    def get_vehicle(self):
        return self.__vehicle

    def get_date(self):
        return self.__date

    def get_renter(self):
        return self.__renter

    def __str__(self):
        return (
            f"Renter: {self.__renter} | "
            f"Vehicle: {self.__vehicle.get_model()} "
            f"({self.__vehicle.get_registration_number()}) | "
            f"Date: {self.__date} | "
            f"Price: {self.__vehicle.get_daily_price()} Ft"
        )

from src.models.vehicle import Vehicle

class PassengerCar(Vehicle):

    def __init__(self, registration_number, model, daily_price, seat_count):
        super().__init__(registration_number, model, daily_price)

        self.__seat_count = seat_count

    def get_seat_count(self):
        return self.__seat_count

    def __str__(self):
        return f" {super().__str__()} - Ülőhelyek száma: {self.get_seat_count()} "
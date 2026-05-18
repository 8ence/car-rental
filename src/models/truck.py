from src.models.vehicle import Vehicle


class Truck(Vehicle):

    def __init__(self, registration_number, model, daily_price, load_capacity):
        super().__init__(registration_number, model, daily_price)

        self.__load_capacity = load_capacity

    def get_load_capacity(self):
        return self.__load_capacity

    def __str__(self):
        return f" {super().__str__()} - Teherbirás: {self.__load_capacity} kg"

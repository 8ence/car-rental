class RentalCompany:

    def __init__(self, name):
        self.__name = name
        self.__vehicles = []
        self.__rentals = []

    def get_name(self):
        return self.__name

    def get_vehicles(self):
        return self.__vehicles

    def get_rentals(self):
        return self.__rentals

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def add_rental(self, rental):
        self.__rentals.append(rental)

    def __str__(self):
        return f"{self.__name} - Autók száma: {len(self.__vehicles)}, Bérlések száma: {len(self.__rentals)}"
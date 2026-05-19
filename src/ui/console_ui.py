class ConsoleUi:

    def __init__(self, rental_service, rental_company):
        self.__rental_service = rental_service
        self.__rental_company = rental_company

    def start(self):
        while True:
            print("\n=== Car Rental System ===")
            print("1. List vehicles")
            print("2. Rent vehicle")
            print("3. Cancel rental")
            print("4. List rentals")
            print("0. Exit")

            choice = input("Choose an option (Type the serial number): ")

            if choice == "1":
                self.__list_vehicles()
            elif choice == "2":
                self.__rent_vehicle()
            elif choice == "3":
                self.__cancel_rental()
            elif choice == "4":
                self.__list_rentals()
            elif choice == "0":
                print("Exiting... Goodbye!")
            else:
                print("Invalid option. Please choose one of the options above.")

    def __list_vehicles(self):
        print("\n=== List vehicles ===")
        for vehicle in self.__rental_company.get_vehicles():
            print(vehicle)

    def __rent_vehicle(self):
        try:
            registration_number  = input("Enter registration number: ")
            date = input("Enter date (YYYY-MM-DD): ")
            renter = input("Enter name: ")

            vehicle = self.__find_vehicle_by_registration_number(registration_number.upper())

            price = self.__rental_service.rent_vehicle(vehicle, date, renter)

            print(f"Succesfull rental! Price: {price} Ft")

        except Exception as ex:
            print(ex)

    def __cancel_rental(self):
        try:
            registration_number = input("Enter registration number: ")
            date = input("Enter date (YYYY-MM-DD): ")

            vehicle = self.__find_vehicle_by_registration_number(registration_number.upper())

            message = self.__rental_service.cancel_rental(vehicle, date)

            print(message)

        except Exception as ex:
            print(ex)

    def __list_rentals(self):
        try:
            print("\n=== List rentals ===")
            for rental in self.__rental_service.list_rentals():
                print(rental)

        except Exception as ex:
            print(ex)

    def __find_vehicle_by_registration_number(self, registration_number):

        for vehicle in self.__rental_company.get_vehicles():

            if vehicle.get_registration_number() == registration_number:
                return vehicle

        raise Exception("Invalid registration number")

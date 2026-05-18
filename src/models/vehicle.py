from abc import ABC


class Vehicle(ABC):

    def __init__(self, registration_number, model, daily_price):
        self.__registration_number = registration_number
        self.__model = model
        self.__daily_price = daily_price

    def get_registration_number(self):
        return self.__registration_number

    def get_model(self):
        return self.__model

    def get_daily_price(self):
        return self.__daily_price

    def __str__(self):
        return f"{self.__registration_number}-{self.__model}-{self.__daily_price} Ft"

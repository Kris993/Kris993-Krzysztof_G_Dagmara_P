class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count

    @property
    def car_mass(self):
        return self.__car_mass

    @car_mass.setter
    def car_mass(self, mass):
        if mass > 2000:
            raise IllegalCarError("The car is too heavy")
        else:
            self.__car_mass = mass

    @property
    def pax_count(self):
        return self.__pax_count

    @pax_count.setter
    def pax_count(self, passengers):
        if passengers > 5 or passengers < 1:
            raise IllegalCarError("In the car is too many passengers or with any passengers")
        else:
            self.__pax_count = passengers

    def count_total_mass(self):
        return self.car_mass + self.pax_count * 70


class IllegalCarError(ValueError):
    pass

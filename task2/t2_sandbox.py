from abc import ABC, abstractmethod
from math import pi

class Run(ABC):
    '''
     self.runners = runners
        # string of only 2 vals: 'short' for short races, 'long' marathon
        self.race_type = "short"
        # positive float val
        self.distance = distance
        # only for marathons: energy consumed/km of marathon
        self.energy_per_km = 100
    '''
    
    def __init__(self, name: str, race_type: str, distance: float, runners: list = None):
        self.name = name
        self.race_type = race_type
        self.distance = distance
        self.runners = []
        
    def get_name(self):
        return self.name

    @abstractmethod
    def get_runner_list(self):
        pass
    @abstractmethod
    def get_race_type(self):
        pass

    @abstractmethod
    def get_distance(self):
        pass

class RaceOne(Run):

    def get_runner_list(self):
        return self.runners
    
    def get_race_type(self):
        rtype = input("race type is:")
        self.race_type = rtype

    def get_distance(self):
        distance = float(input('enter distance: '))
        return distance

class RaceTwo(Run):

    def get_area(self):
        return pi*(self.shape_data**2)

    def get_perimeter(self):
        return 2*pi*self.shape_data

my_race = Circle('my circle', 3)
print("The runner " + .get_name() + " is: " + str(my_circle.get_area()))
print("The perimeter of " + my_circle.get_name() + " is: " + str(my_circle.get_perimeter()))

my_square = Square('my square', 3)
print("The area of " + my_square.get_name() + " is: " + str(my_square.get_area()))
print("The perimeter of " + my_square.get_name() + " is: " + str(my_square.get_perimeter()))
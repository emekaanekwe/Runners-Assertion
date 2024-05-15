'''PURPOSE'''
#Create a structure to hold information about 
    # races and process racing data

from custom_errors import *

class Runner:
    def __init__(self, name: str, age: int, country, sprint_speed: float, endurance_speed: float):
        max_energy = 1000
        self.name = name
        # between 5-20 inclusive
        self.age = age
        # from the .csv file
        self.country = country
        # between 2.2-6.8 inclusive
        self.sprint_speed = sprint_speed
        # between 1.8-5.4 meters per second inclusive
        self.endurance_speed = endurance_speed
        # current level of energy
        self.energy = max_energy
    
    
    # return the value of energy and check the value's params
    def drain_energy(self, drain_points) -> int:
        assert self.energy < 0, "energy cannot be less than 0"
        assert drain_points < 0, "drain_points cannot be less than 0"
        assert drain_points > self.energy, "drain_points cannot be higher than max energy"
        self.energy -= drain_points
        assert self.energy < 0, "energy cannot be less than 0"
        return self.energy
    
    # check recovery value's params
    def recover_energy(self, recovery_amount):
        assert recovery_amount > 1000, "cannot be over 1000"
        self.energy += recovery_amount
        if self.energy > 1000:
            self.energy = 1000
        
    # make a dict to st race type and distance    
    def run_race(self, race_type, distance) -> float:
        race_dict = {'race_type': race_type, 'distance': distance}        
        return race_dict['distance'] * self.sprint_speed
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"

    def valid_inputs(self):
        pass
    
if __name__ == '__main__':
    runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    
    # running a short race
    time_taken = runner.run_race('short', 2)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")
    



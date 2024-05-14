from custom_errors import *

class Runner:
    def __init__(self, name, age, country, sprint_speed, endurance_speed):
        max_energy = 1000
        self.name = name
        self.age = age
        self.country = country
        self.sprint_speed = sprint_speed
        self.endurance_speed = endurance_speed
        self.energy = max_energy
    
    def drain_energy(self, drain_points):
        self.energy -= drain_points
    
    def recover_energy(self, recovery_amount):
        self.energy += recovery_amount
    
    def run_race(self, race_type, distance):
        race_type = 'short'
        return distance * self.sprint_speed

if __name__ == '__main__':
    runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    
    # running a short race
    time_taken = runner.run_race('short', 2)
    print(f"Runner {runner.name} took {time_taken} seconds to run 2km!")
    



from custom_errors import *
from abc import ABC, abstractmethod
from runner import Runner
import math

class Race(ABC):
    def __init__(self, distance, runners = None):
        self.runners = []
        self.race_type = "short"
        self.distance = distance
        self.energy_per_km = 100
    
    def add_runner(self, runner):
        self.runners.append(runner)
    
    def remove_runner(self, runner):
        self.runners.remove(runner)
    
    def conduct_race(self):
        result = []
        if self.race_type == "short":
            for i, runner in enumerate(self.runners):
                time_taken = runner.run_race("short", 1) * 1.2
                result.append((runner, time_taken))
        elif self.race_type == "long":
            for i, runner in enumerate(self.runners):
                time_taken = 0
                for km in range(math.ceil(self.distance)):
                    if runner.energy > 0:
                        time_taken += runner.run_race("long", self.distance)
                        runner.drain_energy(100)
                    else:
                        time_taken = 'DNF'
                        break
                result.append((runner, time_taken))
        return result

class ShortRace:
    # Why do we even have these? These are so silly
    def __init__(self, distance, runners = None):
        self.runners = []
        self.race_type = "short"
        self.distance = distance
        self.energy_per_km = 100
        self.maximum_participants = 8
        self.time_multiplier = 1.2
    
    def add_runner(self, runner):
        self.runners.append(runner)
    
    def remove_runner(self, runner):
        self.runners.remove(runner)
    
    def conduct_race(self):
        result = []
        if self.race_type == "short":
            for i, runner in enumerate(self.runners):
                time_taken = runner.run_race("short", 1) * 1.2
                result.append((runner, time_taken))
        elif self.race_type == "long":
            for i, runner in enumerate(self.runners):
                time_taken = 0
                for km in range(math.ceil(self.distance)):
                    if runner.energy > 0:
                        time_taken += runner.run_race("long", self.distance)
                        runner.drain_energy(100)
                    else:
                        time_taken = 'DNF'
                        break
                result.append((runner, time_taken))
        return result


class MarathonRace:
    # Why do we even have these? These are so silly
    def __init__(self, distance, runners = []):
        self.runners = []
        self.race_type = "long"
        self.distance = distance
        self.energy_per_km = 100
        self.maximum_participants = 16
        self.time_multiplier = 1.2
    
    def add_runner(self, runner):
        self.runners.append(runner)
    
    def remove_runner(self, runner):
        self.runners.remove(runner)
    
    def conduct_race(self):
        result = []
        if self.race_type == "short":
            for i, runner in enumerate(self.runners):
                time_taken = runner.run_race("short", 1) * 1.2
                result.append((runner, time_taken))
        elif self.race_type == "long":
            for i, runner in enumerate(self.runners):
                time_taken = 0
                for km in range(math.ceil(self.distance)):
                    if runner.energy > 0:
                        time_taken += runner.run_race("long", self.distance)
                        runner.drain_energy(100)
                    else:
                        time_taken = 'DNF'
                        break
                result.append((runner, time_taken))
        return result
        
if __name__ == '__main__':
    short_race = ShortRace(0.5)
    long_race = MarathonRace(5.0)

    # Add a Runner
    eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)

    long_race.add_runner(eli)
    long_race.add_runner(rup)

    result = long_race.conduct_race()
    print(result)

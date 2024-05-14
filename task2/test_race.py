import unittest
from custom_errors import RunnerAlreadyExistsError, RunnerDoesntExistError
from race import Race, ShortRace, MarathonRace
from runner import Runner

class TestRaces(unittest.TestCase):

    def test_init(self):
        # Test successful initialization for short race
        short_race = ShortRace(0.5, [])
        self.assertEqual(short_race.race_type, 'short')
        self.assertEqual(short_race.distance, 0.5)
        self.assertEqual(short_race.runners, [])
        self.assertEqual(short_race.maximum_participants, 8)
        self.assertEqual(short_race.time_multiplier, 1.2)
        
        # Test successful initialization for marathon
        marathon_race = MarathonRace(42.0, [])
        self.assertEqual(marathon_race.race_type, 'long')
        self.assertEqual(marathon_race.distance, 42)
        self.assertEqual(marathon_race.runners, [])
        self.assertEqual(marathon_race.maximum_participants, 16)
        self.assertEqual(marathon_race.energy_per_km, 100)
    
    def test_add_runner(self):
        # Create a short race and a runner
        short_race = ShortRace(0.5, [])
        runner = Runner('Lauren', 20, 'Australia', 2.4, 2.4)
        
        # Test adding a new runner
        short_race.add_runner(runner)
        self.assertIn(runner, short_race.runners)
        
        # Test exceeding maximum participants
        for i in range(short_race.maximum_participants - 1):
            short_race.add_runner(Runner(f'Runner {i}', 10, 'Azerbaijan', 3.2, 2.2))
    
    def test_remove_runner(self):
        # Create a short race and a runner
        short_race = ShortRace(5.0, [])
        runner = Runner('Yaakov', 20, 'Switzerland', 2.4, 2.4)
        short_race.add_runner(runner)
        
        # Test removing an existing runner
        short_race.remove_runner(runner)
        self.assertNotIn(runner, short_race.runners)
    
    def test_conduct_race_short(self):
        # Create a short race and runners
        short_race = ShortRace(5.0, [])
        runner1 = Runner('John', 10, 'Australia', 2.8, 2.8)
        runner2 = Runner('Jane', 12, 'Australia', 4.2, 4.5)
        short_race.add_runner(runner1)
        short_race.add_runner(runner2)
        
        # Conduct the race and get the results
        results = short_race.conduct_race()
        
        # Check the results
        self.assertIsInstance(results, list, f"Results returned from short race's conduct race should be a list")
        list_of_racer_names = [x.name for x in [y[0] for y in results]]
        self.assertIn("John", list_of_racer_names, f"Runner John expected in results but not found")
        self.assertIn("Jane", list_of_racer_names, f"Runner Jane expected in results but not found")
        
    def test_conduct_race_marathon(self):
        # Create a marathon race and runners
        marathon = MarathonRace(42.0, [])
        runner1 = Runner('John', 10, 'Australia', 2.8, 2.8)
        runner2 = Runner('Jane', 12, 'Australia', 3.2, 5.2)
        marathon.add_runner(runner1)
        marathon.add_runner(runner2)
        
        # Conduct the race and get the results
        results = marathon.conduct_race()
        
        # Check the results
        self.assertIsInstance(results, list, f"Results returned from short race's conduct race should be a list")
        list_of_racer_names = [x.name for x in [y[0] for y in results]]
        self.assertIn("John", list_of_racer_names, f"Runner John expected in results but not found")
        self.assertIn("Jane", list_of_racer_names, f"Runner Jane expected in results but not found")
    
    def test_dnf_handling(self):
        # Create a marathon race and runners
        marathon = MarathonRace(42.0, [])
        runner1 = Runner('John', 10, 'Australia', 2.8, 2.8)
        runner2 = Runner('Jane', 12, 'Australia', 4.2, 4.5)
        marathon.add_runner(runner1)
        marathon.add_runner(runner2)
        
        # Conduct the race and get the results
        results = marathon.conduct_race()
        
        # Both runners should run out of energy and get 'DNF'
        self.assertIsInstance(results, list, f"Results returned from short race's conduct race should be a list")
        list_of_racer_times = [y[1] for y in results]
        self.assertIn("DNF", list_of_racer_times, f"Runner John should DNF but didn't")

if __name__ == '__main__':
    unittest.main()


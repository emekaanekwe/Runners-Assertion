import unittest
from competition import Competition
from runner import Runner
from custom_errors import CustomTypeError, CustomValueError
from race import Race, ShortRace, MarathonRace


class SimpleShortRace(ShortRace):
    """A simple race implementation to simulate ShortRace"""
    def __init__(self, distance, runners):
        super().__init__(distance, runners)
        
    def conduct_race(self):
        # Return a sorted list of runners based on a simple criterion (e.g., speed)
        return sorted(
            [(runner, self.distance / runner.sprint_speed) for runner in self.runners],
            key=lambda x: x[1]
        )

class SimpleMarathonRace(MarathonRace):
    """A simple race implementation to simulate MarathonRace"""
    def __init__(self, distance, runners):
        super().__init__(distance, runners)
        
    def conduct_race(self):
        # Return a sorted list of runners based on a simple criterion (e.g., speed)
        return sorted(
            [(runner, self.distance / runner.endurance_speed) for runner in self.runners],
            key=lambda x: x[1]
        )

class TestCompetition(unittest.TestCase):

    def setUp(self):
        # Create some runner instances for testing
        self.runners = [
            Runner("Elijah", 19, 'Australia', 6.4, 5.2),
            Runner("Rupert", 67, 'Botswana', 2.2, 1.8),
            Runner("Phoebe", 12, 'France', 3.4, 2.8),
            Runner("Lauren", 13, 'Iceland', 4.4, 5.1),
            Runner("Chloe", 21, 'Timor-Leste', 5.2, 1.9)
        ]
        
        # Set up a competition instance
        self.distances_short = [0.5, 0.6, 1.2]
        self.distances_marathon = [4.0, 11.0, 4.5]
        self.competition = Competition(self.runners, 3, self.distances_short, self.distances_marathon)

    def test_init_valid_input(self):
        # Assert that the competition instance is properly initialized
        self.assertEqual(self.competition.runners, self.runners)
        self.assertEqual(self.competition.rounds, 3)
        self.assertEqual(self.competition.distances_short, self.distances_short)
        self.assertEqual(self.competition.distances_marathon, self.distances_marathon)
        self.assertIsNotNone(self.competition.leaderboard)

    def test_init_invalid_input(self):
        # Test invalid runners list
        with self.assertRaises(CustomTypeError):
            Competition("not a list", 3, self.distances_short, self.distances_marathon)
        
        # Test invalid rounds
        with self.assertRaises(CustomValueError):
            Competition(self.runners, 0, self.distances_short, self.distances_marathon)
        
        with self.assertRaises(CustomValueError):
            Competition(self.runners, 4, self.distances_short, self.distances_marathon)
        
        # Test invalid distance lists
        with self.assertRaises(CustomTypeError):
            Competition(self.runners, 3, "not a list", self.distances_marathon)
        
        with self.assertRaises(CustomTypeError):
            Competition(self.runners, 3, self.distances_short, "not a list")

    def test_conduct_competition(self):
        # Conduct the competition
        leaderboard = self.competition.conduct_competition()

        # Assert the leaderboard is updated correctly
        # This will depend on the input results and implementation of update_leaderboard
        # Example expected leaderboard assuming input data and round outcomes
        expected_leaderboard = {'1st': ('Elijah', 12), 
        '2nd': ('Chloe', 9), 
        '3rd': ('Lauren', 6), 
        '4th': ('Phoebe', 3), 
        '5th': ('Rupert', 0)}
        self.assertEqual(leaderboard, expected_leaderboard, f"Invalid leaderboard. Check points logic {expected_leaderboard}")

    def test_conduct_race(self):
        # Use real race classes for testing
        short_race = SimpleShortRace(0.5, self.runners)
        marathon_race = SimpleMarathonRace(4.0, self.runners)
        
        # Conduct races
        short_result = self.competition.conduct_race(short_race)
        marathon_result = self.competition.conduct_race(marathon_race)
        
        # Verify that results are sorted by time correctly
        # Assuming lower times indicate higher rank
        self.assertLess(short_result[0][1], short_result[1][1])  # 1st should be faster than 2nd
        self.assertLess(marathon_result[0][1], marathon_result[1][1])  # 1st should be faster than 2nd

    def test_update_leaderboard(self):
        # Define test results for updating the leaderboard
        race_results = [(self.runners[0], 10.0), (self.runners[1], 12.0), (self.runners[2], 14.0)]
        self.competition.update_leaderboard(race_results)
        
        # Validate the leaderboard
        expected_leaderboard = {
            '1st': ('Elijah', 2),
            '2nd': ('Rupert', 1),
            '3rd': ('Phoebe', 0),
            '4th': None,
            '5th': None
        }
        self.assertEqual(self.competition.leaderboard, expected_leaderboard)


if __name__ == '__main__':
    unittest.main()


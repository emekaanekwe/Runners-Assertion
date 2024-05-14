import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def test_runner_initialization(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        
        # Check the initialization of attributes
        self.assertEqual(runner.name, 'Elijah')
        self.assertEqual(runner.age, 18)
        self.assertEqual(runner.country, 'Australia')
        self.assertEqual(runner.sprint_speed, 5.8)
        self.assertEqual(runner.endurance_speed, 4.4)
        self.assertEqual(runner.energy, 1000)

if __name__ == '__main__':
    unittest.main()


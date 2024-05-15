import unittest
from runner import Runner

class TestRunner(unittest.TestCase):
    def test_runner_initialization(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        # invalid test case
        # Runner(123, 18, 'Australia', 2.8, 4.4)
        
        # Check the initialization of attributes
        self.assertEqual(runner.name, type(str))
        self.assertEqual(runner.age, 18)
        self.assertEqual(runner.country, 'Australia')
        self.assertEqual(runner.sprint_speed, 5.8)
        self.assertEqual(runner.endurance_speed, 4.4)
        self.assertEqual(runner.energy, 1000)
        self.assertLessEqual(runner.drain_energy())

if __name__ == '__main__':
    unittest.main()


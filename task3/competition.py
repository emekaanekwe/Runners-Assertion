from race import *
from runner import Runner


class Competition:
    MAX_ROUNDS = 3

    def __get_ordinal(self, n):
        # Helper function to return the ordinal string for a given integer
        # NOTE : You can ignore this method, you don't need to comment
        # or do any checks on it whatsoever
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        if 11 <= n % 100 <= 13:
            suffix = 'th'
        else:
            suffix = suffixes.get(n % 10, 'th')
        return f"{n}{suffix}"

    def __init__(self, runners, rounds, distances_short, distances_marathon):
        self.runners = runners
        self.rounds = rounds
        self.distances_short = distances_short
        self.distances_marathon = distances_marathon

        self.leaderboard = {}

        for i in range(1, len(self.runners) + 1):
            self.leaderboard[self.__get_ordinal(i)] = None

    def conduct_competition(self):
        current_round = 1
        i = 0
        while current_round <= self.rounds:
            # Conduct the short race with all runners
            short_race = ShortRace(self.distances_short[i], runners = self.runners)
            short_race.runners = self.runners
            short_result = self.conduct_race(short_race)

            # Conduct the Marathon race with all runners
            marathon = MarathonRace(self.distances_marathon[i], runners = self.runners)
            short_race.runners = self.runners
            marathon_result = self.conduct_race(marathon)

            # Recover energy for all DNF runners
            for runner in self.runners:
                runner.recover_energy(1000)

            current_round += 1
            self.update_leaderboard(short_result)
            self.update_leaderboard(marathon_result)

        return self.leaderboard

    def conduct_race(self, race):
        return race.conduct_race()

    def update_leaderboard(self, results):
        sorted_result = sorted(results, key=lambda x: x[1])
        leaderboard_keys = list(self.leaderboard.keys())
        for i, runner_time in enumerate(sorted_result):
            self.leaderboard[leaderboard_keys[i]] = (runner_time[0].name, len(results) - (i+1))
        

    def print_leaderboard(self):
        print("Leaderboard\n\n")
        for key, value in self.leaderboard.items():
            print(f"{key} - {value[0]} ({value[1]})")

if __name__ == '__main__':
    # Example usage
    runners = [
        Runner("Elijah", 19, 'Australia', 6.4, 5.2),
        Runner("Rupert", 67, 'Botswana', 2.2, 1.8),
        Runner("Phoebe", 12, 'France', 3.4, 2.8),
        Runner("Lauren", 13, 'Iceland', 4.4, 5.1),
        Runner("Chloe", 21, 'Timor-Leste', 5.2, 1.9)
    ]

    competition = Competition(runners, 3, [0.5, 0.6, 1.2], [4.0, 11.0, 4.5])
    _ = (competition.conduct_competition())
    competition.print_leaderboard()

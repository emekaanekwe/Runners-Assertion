def create_runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed):
    return Runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed)

def create_competition(runners, rounds, distances_short, distances_long):
    return Competition(runners, rounds, distances_short, distances_marathon)

def main():
    # Ask the user to create runners (until they decide to add no more)
    runners = []

    # TODO: Take input for several runners until the user choses to quit

    # Ask the user to create a competition
    rounds = None
    distances_short = []
    distances_long = []

    comp = create_competition(runners, rounds, distances_short, distances_long)

    # Conduct the competition
    comp.conduct_competition()

    # Reveal the results!
    comp.print_leaderboard()

if __name__ == '__main__':
    main()


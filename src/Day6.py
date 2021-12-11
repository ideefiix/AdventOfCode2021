
#Task 1 Not very good solution
def population_growth(start_population, days):
    population = start_population[:]

    for day in range(days):
        for i in range(len(population)):
            if population[i] == 0:
                population[i] = 6
                population.append(8)
            else:
                population[i] = population[i] - 1

    return population

#Task 2. Better solution
def population_growth2(start_pop_list, days):
    lanterFishes_per_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Read the start values
    for fish in start_pop_list:
        lanterFishes_per_state[fish] +=  1

    # Update for each day
    for day in range(days):
        births = lanterFishes_per_state[0]
        for state in range(len(lanterFishes_per_state)):
            if state == 0:
                continue
            lanterFishes_per_state[state - 1] += lanterFishes_per_state[state]
            lanterFishes_per_state[state] = 0

        lanterFishes_per_state[6] += births
        lanterFishes_per_state[8] += births
        lanterFishes_per_state[0] -= births

    return sum(lanterFishes_per_state)




if __name__ == '__main__':
    lanternFish = []
    with open('input6.txt', 'r') as file:
        lines = file.readlines()
        list_str = lines[0].strip().split(',')
        for fish in list_str:
            lanternFish.append(int(fish))
    print(population_growth2(lanternFish, 256))
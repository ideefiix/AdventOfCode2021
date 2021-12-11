def fuel_cost(listt, position):
    cost = 0
    for crabPos in listt:
        cost += abs(position - crabPos)
    return cost


if __name__ == '__main__':
    crab_pos = []
    cost_dict = {}
    with open('input7.txt', 'r') as file:
        lines = file.readlines()
        list_str = lines[0].strip().split(',')
        for pos in list_str:
            crab_pos.append(int(pos))

    for position in range(max(crab_pos)):
        cost_dict.update({str(position): fuel_cost(crab_pos, position)})

    pos, cost = min(cost_dict.items(), key= lambda tup: tup[1])
    
    print("Task 1")
    print("Best position is " + str(pos) + " which has a cost of " + str(cost) )

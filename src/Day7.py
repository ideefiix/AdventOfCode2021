def fuel_cost(listt, position):
    cost = 0
    for crabPos in listt:
        cost += abs(position - crabPos)
    return cost

def fuel_cost_task2(listt, position):
    cost = 0
    for crab_pos in listt:
        diff = abs(position - crab_pos)
        for i in range(diff + 1):
            cost += i
    return cost


if __name__ == '__main__':
    crab_pos = []
    cost_dict = {}
    cost_dict2 = {}
    with open('input7.txt', 'r') as file:
        lines = file.readlines()
        list_str = lines[0].strip().split(',')
        for pos in list_str:
            crab_pos.append(int(pos))

    for position in range(max(crab_pos)):
        cost_dict.update({str(position): fuel_cost(crab_pos, position)})
        cost_dict2.update({str(position): fuel_cost_task2(crab_pos, position)})

    pos1, cost1 = min(cost_dict.items(), key= lambda tup: tup[1])
    pos2, cost2 = min(cost_dict2.items(), key= lambda tup: tup[1])
    
    print("Task 1")
    print("Best position is " + str(pos1) + " which has a cost of " + str(cost1) )
    print("--------------")
    print("Task 2")
    print("Best position is " + str(pos2) + " which has a cost of " + str(cost2) )

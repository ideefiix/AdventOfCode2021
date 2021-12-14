
def get_neighbours(spot, spot_index, row_index, playfield):
    neighbours = []
    #Add Upper
    if row_index > 0:
        neighbours.append(playfield[row_index - 1][spot_index])
    #Add lower
    if row_index < len(playfield) - 1:
        neighbours.append(playfield[row_index + 1][spot_index])
    #Add Left
    if spot_index < len(playfield[0]) - 1:
        neighbours.append(playfield[row_index][spot_index + 1])
    #Add Right
    if spot_index > 0:
        neighbours.append(playfield[row_index][spot_index - 1])
    return neighbours


def sum_lowest_points(playfield):
    summ = 0
    for row_index in range(len(playfield)):
        for spot_index in range(len(playfield[row_index])):
            neighbours = get_neighbours(playfield[row_index][spot_index], spot_index, row_index, playfield)

            if playfield[row_index][spot_index] < min(neighbours):
                summ += int(playfield[row_index][spot_index]) + 1
    return summ

def find_spots_in_basin(spot_index, row_index, playfield, pos_in_basin, spot_list=None):

    if not spot_list:
        #Init the list
        spots = [playfield[row_index][spot_index]]
        pos_in_basin[row_index][spot_index] = True
    else:
        spots = spot_list

    currentNum = playfield[row_index][spot_index]

    #Check Upper
    if row_index > 0:
        if currentNum < playfield[row_index - 1][spot_index] and playfield[row_index - 1][spot_index] != 9 and not pos_in_basin[row_index -1 ][spot_index]:
            #Add spot
            spots.append(playfield[row_index - 1][spot_index])
            pos_in_basin[row_index - 1][spot_index] = True

            find_spots_in_basin(spot_index, row_index-1, playfield, pos_in_basin, spots)
        
    #Check lower
    if row_index < len(playfield) - 1:
        if currentNum < playfield[row_index + 1][spot_index] and playfield[row_index + 1][spot_index] != 9 and not pos_in_basin[row_index + 1][spot_index]:
            #Add
            spots.append(playfield[row_index + 1][spot_index])
            pos_in_basin[row_index + 1][spot_index] = True

            find_spots_in_basin(spot_index, row_index + 1, playfield, pos_in_basin, spots)

    #Check Left
    if spot_index < len(playfield[0]) - 1:
        if currentNum < playfield[row_index][spot_index + 1] and playfield[row_index][spot_index + 1] != 9 and not pos_in_basin[row_index][spot_index + 1]:
            #Add
            spots.append(playfield[row_index][spot_index + 1])
            pos_in_basin[row_index][spot_index + 1] = True

            find_spots_in_basin(spot_index + 1, row_index, playfield, pos_in_basin, spots)

    #Check Right
    if spot_index > 0:
        if currentNum < playfield[row_index][spot_index - 1] and playfield[row_index][spot_index - 1] != 9 and not pos_in_basin[row_index][spot_index - 1]:
            #Add
            spots.append(playfield[row_index][spot_index - 1])
            pos_in_basin[row_index][spot_index - 1] = True

            find_spots_in_basin(spot_index - 1, row_index, playfield, pos_in_basin, spots)

    return spots

# playfield will be destoyed after this call
def get_all_basins(playfield):
    basin_list = []
    pos_in_basin = []
    for row in playfield:
        row2 = []
        for num in row:
            row2.append(False)
        pos_in_basin.append(row2)

    for row_index in range(len(playfield)):
        for spot_index in range(len(playfield[row_index])):
            if playfield[row_index][spot_index] == 9: continue
            neighbours = get_neighbours(playfield[row_index][spot_index], spot_index, row_index, playfield)

            if playfield[row_index][spot_index] < min(neighbours):
                # Find the basin
                basin_size = len(find_spots_in_basin(spot_index, row_index, playfield, pos_in_basin))
                basin_list.append(basin_size)
    return basin_list


if __name__ == '__main__':
    playfield = []
    lines = []
    with open('input9.txt', 'r') as file:
        for line in file.readlines():
            row = []
            for number in line.strip():
                row.append(int(number))
            playfield.append(row)
    
    #Task 1 DONE
    answer1 = sum_lowest_points(playfield)
    print(answer1)
    
    #Task 2
    basin_sizes = get_all_basins(playfield)
    first = max(basin_sizes)
    basin_sizes.remove(first)

    second = max(basin_sizes)
    basin_sizes.remove(second)

    third = max(basin_sizes)
    basin_sizes.remove(third)

    print(first * second * third)

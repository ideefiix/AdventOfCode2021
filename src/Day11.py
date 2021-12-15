def do_flash(row_index, num_index, grid, flashed_pos):
    grid[row_index][num_index] = 0
    flashed_pos.append((num_index, row_index))
    flashes = 1

    # Increase and recursivly call flashing neighbours
    #Check Upper
    if row_index > 0:
        grid[row_index - 1][num_index] += 1
        if grid[row_index - 1][num_index] > 9:
            flashes += do_flash(row_index -1, num_index, grid, flashed_pos)
    #Check bottom
    if row_index < len(grid) -1:
        grid[row_index +1][num_index] += 1
        if grid[row_index +1][num_index] > 9:
            flashes += do_flash(row_index +1, num_index, grid, flashed_pos)
    #Check right
    if num_index > 0:
        grid[row_index][num_index -1] += 1
        if grid[row_index][num_index -1] > 9:
            flashes += do_flash(row_index, num_index -1, grid, flashed_pos)
    #Check left
    if num_index < len(grid[row_index]) -1:
        grid[row_index][num_index +1] += 1
        if grid[row_index][num_index +1] > 9:
            flashes += do_flash(row_index, num_index +1, grid, flashed_pos)
    #Check upper left corner
    if row_index != 0 and num_index != len(grid[row_index]) -1:
        grid[row_index - 1][num_index + 1] += 1
        if grid[row_index - 1][num_index + 1] > 9:
            flashes += do_flash(row_index - 1, num_index + 1, grid, flashed_pos)
    #Check upper right corner
    if row_index != 0 and num_index != 0:
        grid[row_index - 1][num_index - 1] += 1
        if grid[row_index - 1][num_index - 1] > 9:
            flashes += do_flash(row_index - 1, num_index - 1, grid, flashed_pos)
    #Check Bottom left corner
    if row_index != len(grid) -1 and num_index != len(grid[row_index]) -1:
        grid[row_index + 1][num_index + 1] += 1
        if grid[row_index + 1][num_index + 1] > 9:
            flashes += do_flash(row_index + 1, num_index + 1, grid, flashed_pos)
    #Check Bottom right corner
    if row_index != len(grid) -1 and num_index != 0:
        grid[row_index + 1][num_index - 1] += 1
        if grid[row_index + 1][num_index - 1] > 9:
            flashes += do_flash(row_index + 1, num_index - 1, grid, flashed_pos)

    return flashes



def step(grid, steps):
    flashed_pos = []
    flashes = 0

    for stepp in range(steps):
        # add 1 
        for row in grid:
            for num_index in range(len(row)):
                row[num_index] = row[num_index] + 1
        
        # Do flashes
        for row_index in range(len(grid)):
            for num_index in range(len(grid[row_index])):
                if grid[row_index][num_index] > 9:
                    flashes += do_flash(row_index, num_index, grid, flashed_pos)

        # Reset flashed octupuses
        for x, y in flashed_pos:
            grid[y][x] = 0
        flashed_pos = []

    return flashes

def first_sync_step(grid):
    flashed_pos = []
    octupus_in_grid = len(grid) * len(grid[0])
    step_counter = 0

    for stepp in range(2000): # Just some high num
        step_counter += 1
        # add 1 
        for row in grid:
            for num_index in range(len(row)):
                row[num_index] = row[num_index] + 1
        
        # Do flashes
        for row_index in range(len(grid)):
            for num_index in range(len(grid[row_index])):
                if grid[row_index][num_index] > 9:
                    if octupus_in_grid == do_flash(row_index, num_index, grid, flashed_pos):
                        #FOUND IT
                        return step_counter

        # Reset flashed octupuses
        for x, y in flashed_pos:
            grid[y][x] = 0
        flashed_pos = []

    print("No sync step found")
    return None
    

if __name__ == '__main__':
    grid = []
    with open('input11.txt', 'r') as file:
        for line in file.readlines():
            row = []
            line = line.strip()
            for num in line:
                row.append(int(num))
            grid.append(row)
    #TASK 1
    #flashes = step(grid, 100)
    #print(flashes)

    #TASK 2
    sync_step = first_sync_step(grid)
    print(sync_step)
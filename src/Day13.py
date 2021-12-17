def fold(dots, instruction):
    fold_cord = int(instruction[2:])
    moved_dots = dots.copy()

    #Horizontal fold
    if instruction[0] == 'y':
        for dot in dots:
            if dot[1] > fold_cord:
                new_dot = dot
                # Remove old dot
                moved_dots.discard(dot)
                #print(new_dot)
                new_y = new_dot[1] - (new_dot[1] - fold_cord) * 2
                new_dot = (new_dot[0], new_y)
                moved_dots.add(new_dot)
        
    #Vertical fold
    elif instruction[0] == 'x':
        for dot in dots:
            if dot[0] > fold_cord:
                new_dot = dot
                # Remove old dot
                moved_dots.discard(dot)
                new_x = new_dot[0] - (new_dot[0] - fold_cord) * 2
                new_dot = (new_x, new_dot[1])
                moved_dots.add(new_dot)
    
    return moved_dots

def dot_paint(dots):
    board = []
    x_len = max([x for x, y in dots])
    y_len = max([y for x, y in dots])
    #Create board
    for i in range(y_len + 1):
        row = []
        for j in range(x_len + 1):
            row.append('.')
        board.append(row)

    #Paint letters
    for x, y in dots:
        board[y][x] = 'x'

    #Print board to console
    for i in range(y_len + 1):
        print(board[i])
if __name__ == '__main__':
    inputt = ''
    dots = set()
    fold_instructions = []


    with open('input13.txt', 'r') as file:
        inputt = file.read().splitlines()

    # Add dots and instructions
    for line in inputt:
        line = line.split(' ')
        if not line[0]: continue
        elif len(line) == 1:
            line = line[0].split(',')
            dots.add((int(line[0]), int(line[1])))
        elif len(line) == 3:
            fold_instructions.append(line[2])

    #TASK 1 = 958 
 
    for instruction in fold_instructions:
        dots = fold(dots, instruction)
    print(len(dots))
    dot_paint(dots)
INPUT_FILE = "input2.txt"

#TASK 1
def calculate_depth_horizontal(listt):
    depth, horizontal = 0, 0

    for l in listt:
        tmp = l.split()
        if tmp[0] == "forward":
            horizontal += int(tmp[1])
        elif tmp[0] == "down":
            depth += int(tmp[1])
        elif tmp[0] == "up":
            depth -= int(tmp[1])

    return depth, horizontal

#TASK 2
def calculate_depth_horizontal_NEW(listt):
    depth, horizontal, aim = 0, 0, 0

    for l in listt:
        tmp = l.split()
        if tmp[0] == "forward":
            horizontal += int(tmp[1])
            depth += int(tmp[1]) * aim
        elif tmp[0] == "down":
            aim += int(tmp[1])
        elif tmp[0] == "up":
            aim -= int(tmp[1])

    return depth, horizontal

if __name__ == "__main__":
    inputList = []

    with open(INPUT_FILE) as file:
        for line in file.readlines():
            inputList.append(line)

    depth, horizontal = calculate_depth_horizontal(inputList)
    print("Answer task 1: " + str(depth * horizontal))
    
    depth, horizontal = calculate_depth_horizontal_NEW(inputList)
    print(depth, horizontal)
    print("Answer task 2: " + str(depth * horizontal))
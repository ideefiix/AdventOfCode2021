INPUT_FILE = "input1.txt"

#PART 1
def num_depth_increases(numList):
    count = 0
    prev = numList[0]
    for num in numList:
        if num > prev: count += 1
        prev = num
    
    return count

#PART 2
def num_depth_window(numList):
    count = 0
    prev_sum = numList[0] + numList[1] + numList[2]

    for i in range(len(numList) - 2):
        curr_sum = numList[i] + numList[i + 1] + numList[i + 2]
        if curr_sum > prev_sum: count += 1
        prev_sum = curr_sum

    return count


if __name__ == "__main__":
    numList = []
    with open(INPUT_FILE, "r") as inputFile:
        for line in inputFile.readlines():
            numList.append(int(line))

    print("ANSWER task 1: " + str(num_depth_increases(numList)))
    print("ANSWER task 2: " + str(num_depth_window(numList)))


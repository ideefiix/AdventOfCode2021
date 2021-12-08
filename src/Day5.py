

def add_overlap(points, vLine):
    x_diff = abs(int(vLine[0])-int(vLine[2]))
    y_diff = abs(int(vLine[1])-int(vLine[3]))

    x_start = min(int(vLine[0]), int(vLine[2]))
    y_start = min(int(vLine[1]), int(vLine[3]))

    # Don't consider this case yet
    if x_diff != 0 and y_diff != 0: return

    for i in range(x_diff):
        if str(x_start)


if __name__ == '__main__':
    vent_list = []
    points = {}
    with open('input5.txt', 'r') as file:
        for line in file.readlines():
            vent_line = line.strip().replace(' -> ', ',').split(',')
            vent_list.append(vent_line)
            print(vent_list)
        
    for v in vent_list:
        add_overlap(points, v)
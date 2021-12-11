

def add_overlap(points, vLine):
    x_diff = abs(int(vLine[0])-int(vLine[2]))
    y_diff = abs(int(vLine[1])-int(vLine[3]))

    x_start = min(int(vLine[0]), int(vLine[2]))
    y_start = min(int(vLine[1]), int(vLine[3]))

    # Diagonal Path
    if x_diff != 0 and y_diff != 0: 
        x_increases = vLine[2] > vLine[0]
        y_increases = vLine[3] > vLine[1]
        # Case 1:
        # \
        #  \
        #   \
        if x_increases == y_increases:
            for i in range(x_diff + 1):
                point = str(x_start + i) + "/" + str(y_start + i)
                if point in points:
                    points[point] = points[point] + 1
                else:
                    points.update({point: 1})
        # Case 2
        #   /
        #  /
        # /
        if x_increases != y_increases:
            y_max = max(int(vLine[1]), int(vLine[3]))
            for i in range(x_diff + 1):
                point = str(x_start + i) + "/" + str(y_max - i)
                if point in points:
                    points[point] = points[point] + 1
                else:
                    points.update({point: 1})
        return

    #Horizontal Path
    if x_diff != 0:
        for i in range(x_diff + 1):
            point = str(x_start + i) + "/" + str(y_start)
            if point in points:
                points[point] = points[point] + 1
            else:
                points.update({point: 1})

    #Vertical Path
    if y_diff != 0:
        for j in range(y_diff + 1):
            point = str(x_start) + "/" + str(y_start + j)
            if point in points:
                points[point] = points[point] + 1
            else:
                points.update({point: 1})

if __name__ == '__main__':
    vent_list = []
    points = {}
    with open('input5.txt', 'r') as file:
        for line in file.readlines():
            vent_line = line.strip().replace(' -> ', ',').split(',')
            vent_list.append(vent_line)
    
    #test_list = [['1', '4', '3', '4'], ['2','1','2','6'], ['1','1','4','4'], ['1', '5', '4', '2'],['4', '2', '1', '5']]
    for v in vent_list:
        add_overlap(points, v)
    dangerPoints = [p for p in points if points[p] >= 2]
    print(len(dangerPoints))



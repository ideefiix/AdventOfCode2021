import math

def get_neighbour(pos, playfield_size):
    neighbours = []
    pos = pos.split(',')
    x, y = int(pos[0]), int(pos[1])
    if x > 0:
        neighbours.append(str(x - 1) + ',' + str(y))
    if x < playfield_size - 1:
        neighbours.append(str(x + 1) + ',' + str(y))
    if y > 0:
        neighbours.append(str(x) + ',' + str(y - 1))
    if y < playfield_size - 1:
        neighbours.append(str(x) + ',' + str(y + 1))
    return neighbours
    
# The algoritm works but it slow af. Something is wrong
def dijkstras(start, stop, playfield, playfield_size):
    vertices = []
    distance = {}
    prev = {}

    for vertex in playfield.keys():
        distance.update({vertex: 999999})
        prev.update({vertex: None})
        vertices.append(vertex)
    distance.update({start: 0})

    while vertices:
        tup = []
        for v in vertices:
            tup.append((v, distance[v]))

        ver, dis = min(tup, key=lambda x: x[1])
        print(ver)
        #Return on reached stop
        if ver == stop: return dis

        vertices.remove(ver)
        for neighbour in get_neighbour(ver, playfield_size):
            alt = distance.get(ver) + playfield[neighbour]
            if alt < distance[neighbour]:
                distance.update({neighbour: alt})
                prev.update({neighbour: ver})


def make_playfield_bigger(playfield):
    side_len = math.sqrt(len(playfield))
    # Increase width by 5
    for ver in list(playfield.keys()):
        pos = ver.split(',')
        x, y = int(pos[0]), int(pos[1])
        for increase in range(1, 5):
            newX = x + int(side_len * increase)
            newVal = (playfield[ver] + increase) % 9
            if newVal == 0: newVal = 9

            coord = str(newX) + ',' + str(y)
            playfield.update({coord: newVal})

    #Increase height by 5
    for ver in list(playfield.keys()):
        pos = ver.split(',')
        x, y = int(pos[0]), int(pos[1])
        for increase in range(1, 5):
            newY = y + int(side_len * increase)
            newVal = (playfield[ver] + increase) % 9
            if newVal == 0: newVal = 9

            coord = str(x) + ',' + str(newY)
            playfield.update({coord: newVal})

    #Used for debugging
def plot_playfield(playfield):
    side_len = int(math.sqrt(len(playfield)))
    for row_index in range(side_len):
        row = []
        for point_index in range(side_len):
            key = str(point_index) + ',' + str(row_index)
            row.append(playfield[key])
        print(row)

if __name__ == "__main__":
    playfield = {} 
    with open('input15.txt', 'r') as file:
        inputt = file.read().splitlines()

    for row_index in range(len(inputt)):
        for x_index in range(len(inputt[row_index])):
            pos = str(x_index) + ',' + str(row_index)
            playfield.update({pos: int(inputt[row_index][x_index])}) 

    # Make playfield 5 times bigger. It must be a square
    make_playfield_bigger(playfield)
    side_len = int(math.sqrt(len(playfield)))
    print(side_len)

    # Find shortest path
    goal = str(side_len - 1) + ',' + str(side_len - 1)
    shortest_path = dijkstras('0,0', goal, playfield, side_len)
    print(shortest_path)



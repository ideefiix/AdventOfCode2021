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

        #Return on reached stop
        if ver == stop: return dis

        vertices.remove(ver)
        for neighbour in get_neighbour(ver, playfield_size):
            alt = distance.get(ver) + playfield[neighbour]
            if alt < distance[neighbour]:
                distance.update({neighbour: alt})
                prev.update({neighbour: ver})

TODO
def make_playfield_bigger(playfield, old_length):
    old_keys = playfield.keys()[:]
    for ver in playfield.keys():
        pos = ver.split(',')
        x, y = pos[0], pos[1]
        for increase in range(1, 5):
            newX = x + increase
            newY = y + increase

            if newX > 9: newX = 1
            if newY > 9: newY = 1
            newPos


if __name__ == "__main__":
    playfield = {} 
    with open('input15.txt', 'r') as file:
        inputt = file.read().splitlines()

    for row_index in range(len(inputt)):
        for x_index in range(len(inputt[row_index])):
            pos = str(x_index) + ',' + str(row_index)
            playfield.update({pos: int(inputt[row_index][x_index])}) 

    # Make playfield 5 times bigger
    playfield_size = len(inputt)
    make_playfield_bigger(playfield, playfield_size)
    new_size = 5 * playfield_size

    # Find shortest path
    goal = str(new_size - 1) + ',' + str(new_size - 1)

    shortest_path = dijkstras('0,0', goal, playfield, new_size)
    print(shortest_path)



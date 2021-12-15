def find_paths_between(vertices, start, goal, illegal_vertices=[]):
    paths = 0
    illegal_vert_copy = illegal_vertices[:]

    # If vertex is lowercase. Never visit it again
    if start.islower():
        illegal_vert_copy.append(start)

    for ver in vertices[start]:
        if ver in illegal_vert_copy: 
            continue
        elif ver == goal: 
            paths += 1
            continue
        else:
            paths += find_paths_between(vertices, ver, goal, illegal_vert_copy)

    return paths

def find_paths_task2(vertices, start, goal, illegal_vertices=[], used_cave_twice=False):
    paths = 0
    illegal_vert_copy = illegal_vertices[:]
    twice_used = used_cave_twice

    # If vertex is lowercase. Add it to visited list
    if start.islower():
        illegal_vert_copy.append(start)
        
    for ver in vertices[start]:
        if ver == "start":
            continue
        elif ver in illegal_vert_copy and twice_used == True: 
            continue
        elif ver in illegal_vert_copy and twice_used == False:  
            paths += find_paths_task2(vertices, ver, goal, illegal_vert_copy, True)
        elif ver == goal: 
            paths += 1
        else:
            paths += find_paths_task2(vertices, ver, goal, illegal_vert_copy, twice_used)

    return paths


if __name__ == '__main__':
    # {a: [b, c]}
    vertices = {}
    inputt = ''
    # Read file
    with open('input12.txt', 'r') as file:
        inputt = file.read()

    # Add vertices and edges
    for line in inputt.splitlines():
        ver = line.split('-')

        if ver[0] in vertices:
            vertices[ver[0]].append(ver[1])
        else:
            vertices.update({ver[0]: [ver[1]]})

        if ver[1] in vertices:
            vertices[ver[1]].append(ver[0])
        else:
            vertices.update({ver[1]: [ver[0]]})

    # Get num of paths
    num_paths = find_paths_between(vertices, 'start', 'end')
    print(num_paths)
    # Get num of paths task2
    num_paths2 = find_paths_task2(vertices, 'start', 'end')
    print(num_paths2)
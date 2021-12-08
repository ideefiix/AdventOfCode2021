
if __name__ == '__main__':
    vent_list = []
    playfield = []
    with open('input5.txt', 'r') as file:
        for line in file.readlines():
            vent_line = line.strip().replace(' -> ', ',').split(',')
            vent_list.append(vent_line)
            print(strr)
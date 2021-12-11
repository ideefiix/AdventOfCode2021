

if __name__ == '__main__':
    crab_pos = []
    with open('input7.txt', 'r') as file:
        lines = file.readlines()
        list_str = lines[0].strip().split(',')
        for pos in list_str:
            crab_pos.append(int(pos))
    
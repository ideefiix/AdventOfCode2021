

def read_data(TXT_FILE="input4.txt"):
    lines = []
    with open(TXT_FILE, 'r') as file:
        lines = file.readlines()

    # READ DRAW-ORDER
    board_list = []
    draw_list = lines[0].split(',')
    draw_list[-1] = draw_list[-1].replace('\n','')

    new_board = True
    curr_board_rows = []
    #READ BOARDS
    for line in lines[2:]: 
        row = line.strip().replace('  ', ' ').split(' ')

        if len(row) > 1:
            if new_board:
                curr_board_rows = []
                curr_board_rows.append(row)
                new_board = False
            else:
                curr_board_rows.append(row)
        else:
            board_list.append(curr_board_rows)
            new_board = True
    #ADD LAST BOARD
    board_list.append(curr_board_rows)

    return draw_list, board_list

def board_won(board):
    for i in range(5):
        for j in range(5):
            
        


def find_board_winner(draws, boards):
    for num in draws:
        for board in boards:
            for row in board:
                for n in row:
                    if n == num:
                        board[row][n] = 'X'
                        if board_won(board):
                            return board


if __name__ == "__main__":
    draw_list, board_list = read_data()

    
   


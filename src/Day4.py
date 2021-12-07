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

def board_has_won(board):
    for i in range(5):
        row = []
        col = []
        for j in range(5):
            row.append(board[i][j])
            col.append(board[j][i])
        row = [x for x in row if x == 'X' ]
        col = [x for x in col if x == 'X' ]
        if len(row) == 5 or len(col) == 5:
            return True
    return False
        


def winner_board_w_winner_draw(draws, boards):
    for num in draws:
        for board in range(len(boards)):
            for row in range(5):
                for n in range(5):
                    if boards[board][row][n] == num:
                        boards[board][row][n] = 'X'
                        if board_has_won(boards[board]):
                            return board, num

def calculate_win_score(board, multiplier):
    numList = []
    for i in range(5):
        for j in range(5):
            if board[i][j].isdigit(): numList.append(int(board[i][j]))
    return sum(numList) * multiplier

# TASK2 method
def loser_board_w_winner_draw(draws, boards):
    board_winners = set()
    for num in draws:
        for board in range(len(boards)):
            for row in range(5):
                for n in range(5):
                    if boards[board][row][n] == num:
                        boards[board][row][n] = 'X'
                        if board_has_won(boards[board]):
                            board_winners.add(board)
                            if len(board_winners) == len(boards):
                                return board, num

if __name__ == "__main__":
    draw_list, board_list = read_data()
    winner_board_index, lastNum = winner_board_w_winner_draw(draw_list, board_list)
    print("TASK 1")
    print("Pick board nr " + str(winner_board_index + 1) + " in order to defeat the squid!")
    print("Your score will be: " + str(calculate_win_score(board_list[winner_board_index], int(lastNum))))

    print("-------------------")

    print("TASK 2")
    loser_board_index, loseNum = loser_board_w_winner_draw(draw_list, board_list)
    print("Pick board nr " + str(loser_board_index + 1) + " in order to always lose to the squid!")
    print("Your score will be: " + str(calculate_win_score(board_list[loser_board_index], int(loseNum))))
    
   


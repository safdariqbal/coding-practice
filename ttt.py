class Board(object):

    def __init__(self):
        self.board = [['-','-','-'], ['-','-','-'],['-','-','-']]

    def add_token(self, row, col, token):
        #if row < 0 or row >= len(self.board):
        #    return
        #if col < 0 or col >= len(self.board[0]):
        #    return
        #if token != 'O' or token != 'X':
        #    return
        self.board[row][col] = token

    def print_board(self):
        board_str = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                board_str += self.board[row][col]
                if col != len(self.board[row])-1:
                    board_str += "|"
            board_str += "\n"
        print board_str

    def is_full(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == '-':
                    return False
        return True
        
class AI(object):

    def make_move(self, board):
        if board.is_full():
            return None
        for row in range(len(board.board)):
            for col in range(len(board.board[row])):
                if board.board[row][col] == '-':
                    return (row, col)


def game_loop():

    board = Board()
    ai = AI()

    while not board.is_full():
        print "Here's the board"
        board.print_board()
        print

        print "Enter the row for your move:",
        inp_str = raw_input()
        row = int(inp_str)
        
        print "Enter the column for your move:",
        inp_str = raw_input()
        col = int(inp_str)

        board.add_token(row-1,col-1, 'X')

        ai_move = ai.make_move(board)
        board.add_token(ai_move[0], ai_move[1], 'O')

        print

if __name__ == "__main__":
    game_loop()

#b = Board()
#b.add_token(0,0,'O') 
#b.add_token(0,1,'O')
#b.add_token(0,2,'O') 
#b.add_token(1,0,'X')
#b.add_token(1,1,'X')
#b.add_token(1,2,'X')
#b.add_token(2,0,'X')
#b.print_board()

#print b.is_full()
#print

#ai = AI()
#print ai.make_move(b)

#b.add_token(2,1,'X')
#print ai.make_move(b)



#b.add_token(2,2,'O')
#b.print_board()

#print b.is_full()

from collections import deque

def get_neighbors(rows, cols, row, col):
    result = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            new_row = row + i
            new_col = row + j
            if new_row >= 0 and new_row < rows and new_col >=0 and new_col < cols:
                result.append((new_row, new_col))
    return result

class Cell:

    def __init__(self, contains_mine):
        self.data = 'M' if contains_mine else 0
        self.revealed = False

class Board:

    def __init__(self, rows, cols, mines):
        self.board = [None] * rows
        for i in xrange(0, rows):
            self.board[i] = [None] * cols
            for j in xrange(0, cols):
                self.board[j] = Cell(False)
        
        for m in mines:
            r = m[0]
            c = m[1]
            self.board[r][c].data = 'M'

    def printBoard(self):
        rows = len(self.board)
        cols = len(self.board[0])
        for i in rows

    def revealCell(self, row, col):

        if self.board[row][col].data == 'M':
            self.board[row][col].revealed = True
            # call print board
            print "Clicked on a Mine!"

        q = deque()
        clicked_cell = self.board[row][col]
        q.append((row, col))
        rows = len(self.board)
        cols = len(self.board[0])

        visited = [None] * rows
        for i in xrange(0, rows):
            visited[i] = [False] * cols
        
        while len(q) > 0:
            cell = q.popleft()

            neighbors = get_neighbors(rows, cols, cell[0], cell[1])

            num_mines = 0
            for n in neighbors:
                if self.board[n[0]][n[1]].data == 'M':
                    num_mines += 1
            
            self.board[row][col].revealed = True
            if num_mines == 0:
                for n in neighbors:
                    r = n[0]
                    c = n[1]
                    if not visited[r][c]:
                        visited[r][c] = True
                        q.append((r,c))





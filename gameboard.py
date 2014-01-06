import sys
class GameBoard(object):

    #initialize board and toroidal flag
    #toroidal means that on edge cells, we wrap around the 
    # board to look for neighbors
    def __init__(self, board, toroidal=False):
        self.validateBoard(board)
        self.board    = board
        self.toroidal = toroidal
    
    def validateBoard(self, unvalidatedBoard):
        if type(unvalidatedBoard) != list:
            raise ValueError("Board given is not a list")

        try:
            for row in unvalidatedBoard:
                for cell in row:
                    if cell > 1 or cell < 0 or type(cell) != int:
                        raise ValueError("Invalid types inside the board")
        except Exception, e:
            raise e



    def simulate(self, n):
        if n < 0:
            raise ValueError("Number of simulations cannot be negative")       

        for i in range(n):
            nextboard = []
            for row in range(len(self.board)):
                temp = []
                for cell in range(len(self.board[row])):
                    temp.append(self.cellFate(row,cell))

                nextboard.append(temp)
            self.board = nextboard

    def getValue(self, row, cell):
        rowbound  = len(self.board)

        #check for cases where the cell is on an edge
        if not self.toroidal:
            if row < 0 or cell < 0:
                return 0
            elif row + 1 > rowbound:
                return 0
            elif cell +1 > len(self.board[row]):
                return 0
        #in case it's toroidal, we have to ensure the 
        #given indeces are within bounds
        cellbound = len(self.board[row % rowbound])

        return self.board[row % rowbound][cell % cellbound]


    def cellFate(self, row, cell):
        currentValue = self.getValue(row,cell)
        liveNeighbors = 0

        #sum each surrounding cell, skip current cell
        surroundModifiers = [-1, 0, +1]
        for i in surroundModifiers:
            for j in surroundModifiers:
                if i == 0 and j == 0:
                    continue
                liveNeighbors += self.getValue(row + i, cell + j)

        if liveNeighbors == 3:
            return 1
        elif liveNeighbors == 2 and currentValue == 1:
            return 1
        return 0

        
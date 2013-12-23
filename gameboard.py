import sys
class GameBoard(object):

    def __init__(self, board, toroidal=False):
        self.board    = board
        self.toroidal = toroidal
    
    def simulate(self):
        if self.board is None:
            return None

        self.nextboard = []
        for row in range(len(self.board)):
            temp = []
            for cell in range(len(self.board[row])):
                temp.append(self.cellFate(row,cell))
                
            self.nextboard.append(temp)

    def getValue(self, row, cell):
        rowbound  = len(self.board)

        #check for cases where the cell is on an edge
        if not self.toroidal:
            if row < 0 or cell < 0:
                return 0
            if row + 1 > rowbound:
                return 0
            if cell +1 > len(self.board[row]):
                return 0
        #in case it's toroidal, we have to ensure the given indeces are within bounds
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
        if liveNeighbors == 2 and currentValue == 1:
            return 1
        return 0

        
import fileinput,sys
from gameboard import GameBoard


def greeting():
    print "\n\rWelcome to the wonderful game of life.\n\r"
    print "Usage:"
    print "Please Enter 1's and 0's delimited by a space."
    print "`python driver.py < $boardfilename.txt` will work if you wish to input a file "

    print "\n\rIf you are manually entering your Life Game board, press CTRL-D"\
          " when you are finished. Thanks!\n\r"

def getFromFile():
    initialGame = list()

    #Looks for file, defaults to stdin if none given
    for line in fileinput.input():
        initialGame.append(cleanAndValidate(line))

    return initialGame
            

def cleanAndValidate(line):
    line = line.rsplit()
    validNums = ["0", "1"]
    result = []
    
    for item in line:
        if item not in validNums:
            #Exit if not 0 or 1
            sys.stderr.write("Please enter a valid cell value. This should be 0 or 1.\n\r")
            exit(1)
        result.append(int(item))

    return result

def printBoard(board):
    for row in board:
        for cell in row:
            sys.stdout.write(str(cell) + " ")
        print ""

def main():
    greeting()
    initialBoard = getFromFile()

    print "You entered:\n\r"

    printBoard(initialBoard)

    g = GameBoard(initialBoard)
    g.simulate()

    print "\n\rThe next generation of this board is:\n\r"

    printBoard(g.nextboard)

if __name__ == '__main__':
    main()
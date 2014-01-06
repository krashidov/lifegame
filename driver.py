import fileinput,sys
from gameboard import GameBoard
import argparse

def greeting():
    description ="\n\rWelcome to the wonderful game of life.\n\rPlease Enter 1's and 0's "\
        "delimited by a space.\n\r`python driver.py $boardfilename.txt` will work "\
        "if you wish to input a file. \n\rIf you are manually entering your Life "\
        "Game board, press Enter and then CTRL-D when you are finished. Thanks!\n\r"

    print description
    parser = argparse.ArgumentParser()

    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                       default=sys.stdin)
    parser.add_argument('--num_generations', '-N', type=int, default=1,
                       help='Number of Generations to simulate the game of life.')
    parser.add_argument('--toroidal', '-T', action='store_true', default=False,
                       help='Simulate the game of life so that edge neighbors wrap around to the opposite side.')

    return parser.parse_args()

def getFromFile(infile):

    initialGame = list()

    #Looks for file, defaults to stdin if none given
    for line in infile:
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
    args = greeting()
    initialBoard = getFromFile(args.infile)

    print "You entered:\n\r"

    printBoard(initialBoard)

    g = GameBoard(initialBoard, args.toroidal)
    g.simulate(args.num_generations)

    print "\n\rAfter " + str(args.num_generations)\
        + " generations, the board will look like:\n\r"

    printBoard(g.board)

if __name__ == '__main__':
    main()
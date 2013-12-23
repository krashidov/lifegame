import unittest
from gameboard import GameBoard

test1 = [[0,1,0,0,0], 
         [1,0,0,1,1], 
         [1,1,0,0,1], 
         [0,1,0,0,0], 
         [1,0,0,0,1]]

test1ans = [[0,0,0,0,0], 
            [1,0,1,1,1], 
            [1,1,1,1,1], 
            [0,1,0,0,0], 
            [0,0,0,0,0]]

test2 = [[0,0,0,0,0], 
         [0,0,0,0,0], 
         [0,0,0,0,0], 
         [0,0,0,0,0], 
         [0,0,0,0,0]]

test3 = [[1]]
test3ans = [[0]]

test4 = [[1,0], 
         [0,1,0,1,0], 
         [0,0,1,0,0,1,0], 
         [1,0,1], 
         [1,0,1,0,1]]

test4ans = [[0,0], 
            [0,1,1,0,0], 
            [0,0,1,1,0,0,0], 
            [0,0,1], 
            [0,0,0,1,0]]

test5 = [[0,0,0,1,0], 
         [0,1,0,0,1], 
         [1,0,0,1,1]]

test5ans = [[0,0,0,0,0], 
            [0,0,1,0,1], 
            [0,0,0,1,1]]


test6 = [[1,1,1,1,1], 
         [1,1,1,1,1], 
         [1,1,1,1,1], 
         [1,1,1,1,1], 
         [1,1,1,1,1]]

test6ans = [[1,0,0,0,1], 
            [0,0,0,0,0], 
            [0,0,0,0,0], 
            [0,0,0,0,0], 
            [1,0,0,0,1]]

test7 = [[1,0,0,0,1], 
         [0,1,0,1,0], 
         [0,0,1,0,0], 
         [0,1,0,1,0], 
         [1,0,0,0,1]]

test7ans = [[0,0,0,0,0], 
            [0,1,1,1,0], 
            [0,1,0,1,0], 
            [0,1,1,1,0], 
            [0,0,0,0,0]]

test8 = [[1,1,1,0]]
test8ans = [[0,1,0,0]]

class TestConway(unittest.TestCase):

    def setUp(self):
        pass

    def test0(self):
        g = GameBoard(test1)
        #testing board property
        self.assertEqual(test1, g.board)

    def test1(self):
        g = GameBoard(test1)
        g.simulate()
        #test in email
        self.assertEqual(test1ans, g.nextboard)

    def test2(self):
        g = GameBoard(test2)
        g.simulate()
        #all zeroes
        self.assertEqual(test2, g.nextboard)

    def test3(self):
        g = GameBoard(test3)
        g.simulate()
        #single digit
        self.assertEqual(test3ans, g.nextboard)

    def test4(self):
        g = GameBoard(test4)
        g.simulate()
        #weird bounds
        self.assertEqual(test4ans, g.nextboard)

    def test5(self):
        g = GameBoard(test5)
        g.simulate()
        # different perimeters
        self.assertEqual(test5ans, g.nextboard)

    def test6(self):
        g = GameBoard(test6)
        g.simulate()
        #all 1s
        self.assertEqual(test6ans, g.nextboard)

    def test7(self):
        g = GameBoard(test7)
        g.simulate()
        #diagnols
        self.assertEqual(test7ans, g.nextboard)

    def test8(self):
        g = GameBoard(test8)
        g.simulate()
        #single row
        self.assertEqual(test8ans, g.nextboard)


if __name__ == '__main__':
    unittest.main()
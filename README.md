#Conway's Game of Life

This is a simple game of life program that simulates generations of Conway's game of life.

Please Enter 1's and 0's delimited by a space.
`python driver.py boardfilename.txt` will work if you wish to input a file.

**If you are manually entering your Life Game board, press Enter and then CTRL-D when you are finished**. Thanks!

usage: driver.py [-h] [--num_generations NUM_GENERATIONS] [--toroidal]
                 [infile]


positional arguments:
  infile


optional arguments:
  * `-h, --help`            show help message and exit
  * `--num_generations NUM_GENERATIONS, -N NUM_GENERATIONS`
                            Number of Generations to simulate the game of life.
  * `--toroidal, -T`        Simulate the game of life so that edge neighbors wrap
                            around to the opposite side.


Examples:
To input a standard board from a file:
`$ python driver.py filewithboard.txt`

To input a standard board from a file, with 4 generations and the toroidal flag set:
`$ python driver.py -T -N 4 filewithboard.txt`

To manually input a board:
`$ python driver.py`
(Press CTRL-D when finished inputting values)

To run unit tests:
`$ python test.py`

Happy Holidays!


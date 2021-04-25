# sudoku
Selection of Sudoku Puzzle Generators written in Python 

## diag_gen.py
Is arguably one of the shittiest Sudoku Puzzles generating algorithm ever invented. Time complexity must be at min like O(n!). It has extremly high probability to dont even terminate or finding any solutions. 
The basic idea behind the implementation is to iterate trough the diagonals of a 9x9 2D List which is initialized with zeros. Alternating between rows and cols until grid is full with numbers. Trying to create random entries coming out of a special lists holing the still possible entries (1,2,..,9), for every column, row and every of the 9 submatrices.
I guess if terminating the solution should be correct but the finding of a valid solution is completely and purely determined by chance. 

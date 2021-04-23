# sudoku
Selection of Sudoku Puzzle Generators written in Python 

## diag_gen.py
Is arguably one of the shittiest Sudoku Puzzles generating algorithm ever invented. Time complexity must be min like O(n!), it has extremly high probability to dont even terminating or finding any solutions. 
Works by iterating trough the diagonals of 9x9 2D List and creating entrys alternating between rows and cols using lists of 0<x<9 for cols, rows and every of the 9 submatrices. I guess if terminating the solution should be correct but the finding of a valid solution is completely determined purely by chance. 

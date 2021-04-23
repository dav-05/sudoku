# sudoku
Selection of Sudoku Puzzle Generators written in Python 

## diag_gen.py
Is arguably the shittiest Sudoku Puzzles generating algorithm ever invented. Complexity must be like O(n!), it has extremly high probability to doesnt even terminating nor finding solutions. 
Works by iterating trough the diagonals of 9x9 2D List and creating entrys alternating between rows and cols using lists of 0<x<9 for cols, rows and every of the 9 submatrices. I guess if terminating the solution should be correct.

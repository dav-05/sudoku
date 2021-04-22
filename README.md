# sudoku
Selection of Sudoku Puzzle Generators written in Python 

## diag_gen.py
Is arguably the shittiest Sudoku Puzzles generating algorithm ever invented. Complexity must be like O(n!), it has extremly high probability to doesnt even terminating nor finding solutions. 
Iteration trough diagonals of 9x9 grid and creating entrys alternating between rows and cols using lists of range(0,9) for cols, rows and every of the 9 submatrices.

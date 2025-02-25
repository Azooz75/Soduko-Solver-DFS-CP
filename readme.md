# Sudoku Solver Project

## Overview
This project is a Sudoku Solver class created in Python to solve Sudoku puzzle arrays.
The solver uses Constraint Propagation, Depth-First-Search (DFS), and backtracking to return a solved Sudoku array.

## Project Structure
- `SudokuSolver.py`: Contains the `sudoku_solver` function which solves the Sudoku puzzles.

## Requirements
- Python 3
- NumPy

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Azooz75/sudoku-solver.git
    cd sudoku-solver
    ```

2. Install the required packages:
    ```sh
    pip install numpy
    pip install copy
   
    ```

## Usage
1. Import the `sudoku_solver` function from the `SudokuSolver` module.
    ```python
   from SudokuSolver import sudoku_solver
    ```
   
2. import dependencies
    ```python
    import numpy as np
    from copy import deepcopy
   ```
   
3. Pass the sudoku solver as an array of any size (9x9, 16x16, etc.) to the `sudoku_solver` function.
    ```python
   puzzle = {
   [8, 5, 2, 9, 7, 6, 2, 4, 3],
   [6, 7, 9, 1, 4, 3, 2, 8, 5],
   [0, 3, 1, 2, 5, 8, 7, 6, 9],
   [3, 1, 4, 5, 2, 7, 8, 9, 6],
   [7, 6, 8, 3, 9, 1, 4, 5, 0],
   [9, 2, 5, 6, 0, 0, 3, 7, 1],
   [5, 4, 3, 8, 6, 2, 9, 1, 7],
   [1, 9, 7, 4, 3, 5, 0, 2, 8],
   [2, 8, 6, 7, 1, 9, 5, 3, 4]
   }
   solution = sudoku_solver(puzzle)
   print(solution)
    ```
4. The `sudoku_solver` function will return the solved Sudoku array.

5. Note: Input array should be a 2D NumPy array with 0s representing empty cells.

## License
MIT License

Copyright (c) 2024 - Mauz Bakri

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
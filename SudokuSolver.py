import numpy as np
from copy import deepcopy

def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """

    class PartialSudokuState:
        def __init__(self, sudoku):
            """Initialises the Sudoku grid"""
            self.n = sudoku.shape[0]
            self.grid_size = int(self.n ** 0.5)

            # Initialises final grid with -1 (empty cells)
            self.final_values = np.full((self.n, self.n), -1, dtype=int)

            # Initialises a 3D array that holds possible values for each cell
            self.possible_values = [[[i+1 for i in range(self.n)] for _ in range(self.n)] for _ in range(self.n)]

            # Initialise the grid with the input sudoku array
            self.init_board()

        def init_board(self):
            """Initialises the board with the pre-set configuration"""
            for row in range(self.n):
                for col in range(self.n):
                    init_value = sudoku[row,col]
                    if init_value != 0 and init_value in self.possible_values[row][col]:
                        self.set_value(row, col, init_value, init=True)
                    elif init_value != 0:
                        # Raises an exception if the initial sudoku state is not valid
                        raise ValueError

        def is_goal(self):
            """Checks if a state is a goal state if every cell has a final value"""
            return np.all(self.final_values > 0)

        def is_invalid(self):
            """Checks if a state is invalid if an empty cell has no more possible values"""
            for row in range(self.n):
                for col in range(self.n):
                    if len(self.possible_values[row][col]) == 0 and self.final_values[row, col] == -1:
                        return True
            return False

        def get_possible_values(self, row, col):
            """Returns an array of possible values for the cell"""
            return self.possible_values[row][col]

        def set_value(self, row, col, value, init=False):
            """Sets the value of a cell and call propagate constraints method"""

            state = self if init else deepcopy(self)

            state.final_values[row, col] = value
            state.possible_values[row][col] = [value]
            state.propagate_constraints(row, col, value)
            return state

        def propagate_constraints(self, row, col, value):
            """Eliminates cell value from possible values in the same row, column, and grid"""

            # Remove value from row and column
            for i in range(self.n):
                try:
                    self.possible_values[row][i].remove(value)
                # Pass is needed in case an exception occurs (if there are no values in the cell we are checking)
                except ValueError:
                    pass
                try:
                    self.possible_values[i][col].remove(value)
                except ValueError:
                    pass

            # Remove value from the corresponding grid
            start_row, start_col = (row // self.grid_size) * self.grid_size, (col // self.grid_size) * self.grid_size
            for i in range(start_row, start_row + self.grid_size):
                for j in range(start_col, start_col + self.grid_size):
                    try:
                        self.possible_values[i][j].remove(value)
                    except ValueError:
                        pass

        def get_next_empty_cell(self):
            """Finds the next empty cell with the fewest possible values (MRV Heuristic)"""
            empty_cells = np.where(self.final_values == -1)
            max_options = self.n + 1
            cell_choice = None
            for row, col in zip(empty_cells[0], empty_cells[1]):
                options = len(self.possible_values[row][col])
                if 1 <= options < max_options:
                    max_options = options
                    cell_choice = (row, col)
            return cell_choice

    def depth_first_search(partial_state):
        """Performs depth first search for possible value selections"""

        cell = partial_state.get_next_empty_cell()
        if cell is None:
            if partial_state.is_goal():
                return partial_state
            else:
                return None

        row, col = cell
        values = partial_state.get_possible_values(row, col)

        for value in values:
            new_state = partial_state.set_value(row, col, value)
            if new_state.is_goal():
                return new_state
            if not new_state.is_invalid():
                result = depth_first_search(new_state)
                if result is not None:
                    return result
        return None

    try:
        partial_state = PartialSudokuState(sudoku)
    # If the initial config is not valid, return a sudoku grid of -1
    except ValueError as e:
        return np.full(sudoku.shape, -1, dtype=int)
    final_state = depth_first_search(partial_state)
    if final_state is not None:
        return final_state.final_values
    else:
        return np.full(sudoku.shape, -1, dtype=int)
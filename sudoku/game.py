import math
import numpy as np
import sudoku.visualize as visualize
from collections import Counter
from typing      import Optional

class Sudoku:

    def __init__(self, size=9):
        """"""
        # Assert size is a square
        if int(math.sqrt(size)) ** 2 != size:
            raise ValueError("'size' should be a square value.")

        # Create grid
        self.grid = np.zeros((size, size), dtype=int)

    ########################################################################
    #                                Move                                  #
    ########################################################################

    def move(self, row: int, column: int, number: int):
        """Play a number on a given row, column.

            Parameters
            ----------
            row : int
                Row on which to play number.

            column : int
                Column on which to play number.

            number : int
                Number to play.
            """
        ####################################################################
        #                              Checks                              #
        ####################################################################

        # Check if number is in range
        if number not in range(self.grid.shape[0]+1):
            raise ValueError(
                f"Number '{number}' out of bounds, should be in range 0-"
                f"{self.grid.shape[0]+1}"
            )

        # Check if cell can be set (i.e., does not contain number)
        if number != 0 and self.grid[row, column] != 0:
            raise ValueError(
                f"Square [{row},{column}] already contains number: "
                f"{self.grid[row, column]}"
            )

        # Set number
        self.grid[row, column] = number

        # Return self
        return self

    ########################################################################
    #                           Check validity                             #
    ########################################################################

    def check(self, array: Optional[np.ndarray] = None) -> bool:
        """Check whether a sudoku is correct or not.

            Parameters
            ----------
            array : np.array of shape=(n, n) or shape=(n,), optional
                Array to check.
                If None is given, check entire sudoku game.

            Returns
            -------
            result : boolean
                True if array is correct, False otherwise.
            """
        # Case of array is None
        if array is None:
            array = self.grid

        # Case of single dimension array
        if array.ndim == 1:
            # Count array
            counts = Counter(array)
            # Remove 0 from counts
            del counts[0]

            # Check whether there are duplicates
            return max(counts.values()) == 1

        # Case of sub-square array
        elif array.shape[0] == array.shape[1] == math.sqrt(self.grid.shape[0]):
            # Flatten sub-square and return case of single dimension array
            return self.check(array.flatten())

        # Case of entire sudoku
        elif array.shape[0] == array.shape[1] == self.grid.shape[0]:
            # Compute square size
            square = int(math.sqrt(self.grid.shape[0]))

            # Get sub-square arrays
            squares = list()
            for slice in np.array_split(self.grid, square):
                squares += [x.T for x in np.array_split(slice.T, square)]

            # Check rows, columns and sub-squares
            return all((
                all(self.check(row   ) for row    in self.grid  ), # Check rows
                all(self.check(column) for column in self.grid.T), # Check columns
                all(self.check(square) for square in squares    ), # Check sub-squares
            ))


    ########################################################################
    #                             I/O methods                              #
    ########################################################################

    @classmethod
    def from_csv(cls, path):
        """Load Sudoku from csv file.

            Parameters
            ----------
            path : Union[str, filehandle]
                Path from which to load csv file.
            """
        # Read grid from csv file
        grid = np.loadtxt(path, delimiter=',', dtype=int)

        # Assert grid is square
        if grid.ndim != 2 or grid.shape[0] != grid.shape[1]:
            raise ValueError(f"Cannot load non-square grid: shape={grid.shape}")

        # Create sudoku class
        sudoku = cls(grid.shape[0])
        # Set sudoku grid
        sudoku.grid = grid

        # Return sudoku
        return sudoku


    def to_csv(self, path):
        """Write sudoku to csv file.

            Parameters
            ----------
            path : Union[str, filehandle]
                Path where to save csv file.
            """
        # Save grid to csv file
        np.savetxt(
            fname     = path,
            X         = self.grid,
            fmt       = '%d',
            delimiter = ',',
        )


    ########################################################################
    #                             Draw puzzle                              #
    ########################################################################

    def show(self, width=3):
        """Show a string representation of sudoku."""
        # Get size of square
        square = int(math.sqrt(self.grid.shape[0]))

        # Draw top row
        result  = visualize.row_top(self.grid, width=width) + '\n'

        # Draw numbers
        for index, row in enumerate(self.grid):
            # Draw numbers
            result += visualize.row_numbers(row, width=width) + '\n'

            # Draw bottom row
            if index == self.grid.shape[0] - 1:
                result += visualize.row_bottom(self.grid, width=width) + '\n'
            # Draw square border
            elif (index + 1) % square == 0:
                result += visualize.square_separator(self.grid, width=width) + '\n'
            # Draw normal border
            else:
                result += visualize.row_separator(self.grid, width=width) + '\n'

        # Print result
        print(result)

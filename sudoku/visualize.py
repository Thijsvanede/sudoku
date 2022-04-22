import math
import numpy as np

def row_top(grid: np.ndarray, width: int = 3) -> str:
    """Draw the top row of a sudoku grid.

        Parameters
        ----------
        grid : np.array of shape=(n_rows, n_rows)
            Grid for which to draw top row.

        width : int, default=3
            Width of the text within a grid square.

        Returns
        -------
        result : str
            Top row of grid.
        """
    # Get size of square in grid
    square = int(math.sqrt(grid.shape[0]))

    # Draw top-left corner
    result = '┏'

    # Draw sub-square
    for index in range(grid.shape[0]):
        # Draw square
        result += '━'*width

        # Draw top-right corner
        if index == grid.shape[0] - 1:
            result += '┓'
        # Draw sub-square border
        elif (index+1) % square == 0:
            result += '┳'
        # Draw normal border
        else:
            result += '┯'

    # Return result
    return result


def row_bottom(grid: np.ndarray, width: int = 3) -> str:
    """Draw the bottom row of a sudoku grid.

        Parameters
        ----------
        grid : np.array of shape=(n_rows, n_rows)
            Grid for which to draw bottom row.

        width : int, default=3
            Width of the text within a grid square.

        Returns
        -------
        result : str
            Bottom row of grid.
        """
    # Get size of square in grid
    square = int(math.sqrt(grid.shape[0]))

    # Draw bottom-left corner
    result = '┗'

    # Draw sub-square
    for index in range(grid.shape[0]):
        # Draw square
        result += '━'*width

        # Draw bottom-right corner
        if index == grid.shape[0] - 1:
            result += '┛'
        # Draw sub-square border
        elif (index+1) % square == 0:
            result += '┻'
        # Draw normal border
        else:
            result += '┷'

    # Return result
    return result


def row_separator(grid: np.ndarray, width: int = 3) -> str:
    """Draw the row separator of a sudoku grid.

        Parameters
        ----------
        grid : np.array of shape=(n_rows, n_rows)
            Grid for which to draw separator row.

        width : int, default=3
            Width of the text within a grid square.

        Returns
        -------
        result : str
            Separator row of grid.
        """
    # Get size of square in grid
    square = int(math.sqrt(grid.shape[0]))

    # Draw left border
    result = '┠'

    # Draw sub-square
    for index in range(grid.shape[0]):
        # Draw square
        result += '─'*width

        # Draw right border
        if index == grid.shape[0] - 1:
            result += '┨'
        # Draw sub-square border
        elif (index+1) % square == 0:
            result += '╂'
        # Draw normal border
        else:
            result += '┼'

    # Return result
    return result


def square_separator(grid: np.ndarray, width: int = 3) -> str:
    """Draw the row separator of a sudoku grid.

        Parameters
        ----------
        grid : np.array of shape=(n_rows, n_rows)
            Grid for which to draw separator row.

        width : int, default=3
            Width of the text within a grid square.

        Returns
        -------
        result : str
            Separator row of grid.
        """
    # Get size of square in grid
    square = int(math.sqrt(grid.shape[0]))

    # Draw left border
    result = '┣'

    # Draw sub-square
    for index in range(grid.shape[0]):
        # Draw square
        result += '━'*width

        # Draw right border
        if index == grid.shape[0] - 1:
            result += '┫'
        # Draw sub-square border
        elif (index+1) % square == 0:
            result += '╋'
        # Draw normal border
        else:
            result += '┿'

    # Return result
    return result


def row_numbers(row: np.ndarray, width: int = 3) -> str:
    """Draw a row of numbers for a sudoku grid.

        Parameters
        ----------
        row: np.array of shape=(n_columns,)
            Row digits to draw.

        width : int, default=3
            Width of the text within a grid square.

        Returns
        -------
        result : str
            Row of grid.
        """
    # Get size of square in grid
    square = int(math.sqrt(row.shape[0]))

    # Draw left border
    result = '┃'

    # Draw sub-square
    for index, number in enumerate(row):
        # Convert number
        number = str(number or ' ')

        # Draw result
        result += f'{number:^{width}}'

        # Add border
        if (index+1) % square == 0:
            result += '┃'
        else:
            result += '│'

    # Draw top-right border
    result = result[:-1] + '┃'

    # Return result
    return result

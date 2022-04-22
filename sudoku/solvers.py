from sudoku.game import Sudoku
import numpy as np

class SolveStrategy:

    def solve(self, game: Sudoku) -> Sudoku:
        """Solve a game with a given strategy.

            Parameters
            ----------
            game : Sudoku
                Sudoku game to solve.

            Returns
            -------
            result : Sudoku
                Solved version of Sudoku game.
            """
        raise NotImplementedError("solve() should be implemented by solver.")


class BasicSolver(SolveStrategy):
    """Basic Sudoku solver."""

    def solve(self, game: Sudoku) -> Sudoku:
        """Solve a game with a basic strategy.

            Parameters
            ----------
            game : Sudoku
                Sudoku game to solve.

            Returns
            -------
            result : Sudoku
                Solved version of Sudoku game.
            """
        # Keep track of changes in grid
        changed = True
        grid    = game.grid.copy()

        # Loop until we don't see changes
        while changed:

            # Loop over each index of grid
            for x in range(game.grid.shape[0]):
                for y in range(game.grid.shape[0]):
                    # Check if square is empty
                    if game.grid[x, y] == 0:
                        # Keep track of possible numbers
                        possible = set()

                        # Loop over all numbers
                        for number in range(1, game.grid.shape[0] + 1):
                            # Play move
                            game = game.move(x, y, number)

                            # Add possible number if correct
                            if game.check():
                                possible.add(number)

                            # Reset move
                            game = game.move(x, y, 0)

                        # If there is a single possible move, play it
                        if len(possible) == 1:
                            game = game.move(x, y, list(possible)[0])

            # Set game grid
            changed = not np.all(grid == game.grid)
            grid    = game.grid.copy()

        # Return game
        return game

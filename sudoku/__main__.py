from sudoku.game    import Sudoku
from sudoku.solvers import BasicSolver

def main():
    # Load sudoku game
    sudoku = Sudoku.from_csv('tmp.csv')
    sudoku.show()

    # Solve game
    solver = BasicSolver()
    sudoku = solver.solve(sudoku)
    sudoku.show()

    print(sudoku.check())

if __name__ == "__main__":
    main()

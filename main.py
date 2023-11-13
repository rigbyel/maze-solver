from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 12, 70, 50, win)
    maze.solve_r(0,0)

    win.wait_for_close()


main()
import enum
import colorama
from lib.maze_world.node import Node, NodeStatus


class WallDirection(enum.Enum):
    Top = 1
    Right = 2
    Botton = 3
    Left = 4


class Maze:
    number_of_rows: int
    number_of_columns: int
    nodes: list[list[Node]]
    start: Node
    goal: Node

    def __init__(self, number_of_rows: int, number_of_columns: int):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns
        self.init_nodes()
        self.start = None
        self.goal = None

    def init_nodes(self):
        nodes = [[Node(j+1, i+1) for i in range(self.number_of_columns)]
                 for j in range(self.number_of_rows)]
        # set outer walls
        for i in range(self.number_of_columns):
            nodes[0][i].border.top = True
            nodes[self.number_of_rows-1][i].border.bottom = True
        for i in range(self.number_of_rows):
            nodes[i][0].border.left = True
            nodes[i][self.number_of_columns-1].border.right = True
        self.nodes = nodes

    def set_start(self, row, column):
        if row < 1 or row > self.number_of_rows:
            raise IndexError("Array index out of bounds!")
        if column < 1 or column > self.number_of_columns:
            raise IndexError("Array index out of bounds!")
        if self.start:
            self.start.status = NodeStatus.Normal
        self.nodes[row-1][column-1].status = NodeStatus.Start
        self.start = self.nodes[row-1][column-1]

    def set_goal(self, row, column):
        if row < 1 or row > self.number_of_rows:
            raise IndexError("Array index out of bounds!")
        if column < 1 or column > self.number_of_columns:
            raise IndexError("Array index out of bounds!")
        if self.goal:
            self.goal.status = NodeStatus.Normal
        self.nodes[row-1][column-1].status = NodeStatus.Goal
        self.goal = self.nodes[row-1][column-1]

    def set_wall(self, row: int, column: int, dir: WallDirection):
        if row < 1 or row > self.number_of_rows:
            raise IndexError("Array index out of bounds!")
        if column < 1 or column > self.number_of_columns:
            raise IndexError("Array index out of bounds!")
        if dir == WallDirection.Top:
            self.nodes[row-1][column-1].border.top = True
            if row != 1:
                self.nodes[row-2][column-1].border.bottom = True
        if dir == WallDirection.Right:
            self.nodes[row-1][column-1].border.right = True
            if column != self.number_of_columns:
                self.nodes[row-1][column].border.left = True
        if dir == WallDirection.Botton:
            self.nodes[row-1][column-1].border.bottom = True
            if row != self.number_of_rows:
                self.nodes[row][column-1].border.top = True
        if dir == WallDirection.Left:
            self.nodes[row-1][column-1].border.left = True
            if column != 1:
                self.nodes[row-1][column-2].border.right = True

    def remove_wall(self, row: int, column: int, dir: WallDirection):
        if row < 1 or row > self.number_of_rows:
            raise IndexError("Array index out of bounds!")
        if column < 1 or column > self.number_of_columns:
            raise IndexError("Array index out of bounds!")
        if dir == WallDirection.Top:
            self.nodes[row-1][column-1].border.top = False
            if row != 1:
                self.nodes[row-2][column-1].border.bottom = False
        if dir == WallDirection.Right:
            self.nodes[row-1][column-1].border.right = False
            if column != self.number_of_columns:
                self.nodes[row-1][column].border.left = False
        if dir == WallDirection.Botton:
            self.nodes[row-1][column-1].border.bottom = False
            if row != self.number_of_rows:
                self.nodes[row][column-1].border.top = False
        if dir == WallDirection.Left:
            self.nodes[row-1][column-1].border.left = False
            if column != 1:
                self.nodes[row-1][column-2].border.right = False

    def print(self):
        colorama.init()

        normal_dash = colorama.Fore.BLACK + "-"
        wall_dash = colorama.Fore.WHITE + "═"
        normal_vertical_line = colorama.Fore.BLACK + "|"
        wall_vertical_line = colorama.Fore.WHITE + "║"
        space = " "
        path_space = colorama.Back.CYAN + " " + colorama.Back.BLACK
        start = colorama.Fore.YELLOW + "S"
        goal = colorama.Fore.GREEN + "G"
        numbers = colorama.Fore.WHITE

        result = colorama.Back.BLACK + space * 3

        # column number
        for i in range(self.number_of_columns):
            result += space * 3 + numbers + str(i+1) + space * 2

        result += "\r\n"

        for i in range(self.number_of_rows):
            result += space * 3

            # top border
            for j in range(self.number_of_columns):
                if self.nodes[i][j].border.top:
                    result += wall_dash * 6
                    if j == self.number_of_columns-1:
                        result += wall_dash
                else:
                    if j != 0 and self.nodes[i][j-1].border.top:
                        result += wall_dash + normal_dash * 5
                    else:
                        result += normal_dash + normal_dash * 5
                    if j == self.number_of_columns-1:
                        result += normal_dash

            result += "\r\n" + numbers + \
                str(i+1) + space * 2 + wall_vertical_line

            # right border
            for j in range(self.number_of_columns):
                if self.nodes[i][j].status == NodeStatus.Start:
                    result += space * 2 + start + space * 2
                elif self.nodes[i][j].status == NodeStatus.Goal:
                    result += space * 2 + goal + space * 2
                else:
                    if self.nodes[i][j].status == NodeStatus.InPath:
                        result += space + path_space * 3 + space
                    else:
                        result += space * 5

                if self.nodes[i][j].border.right:
                    result += wall_vertical_line
                else:
                    result += normal_vertical_line

            result += "\r\n"

        result += space * 3 + wall_dash * 6 * self.number_of_columns + wall_dash
        print(result)

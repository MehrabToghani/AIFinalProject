import enum


class NodeStatus(enum.Enum):
    Blank = 0
    X = 1
    O = 2


class Node:
    row: int
    column: int
    status: NodeStatus

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.status = NodeStatus.Blank


class GameStatus(enum.Enum):
    GameOver = 0
    XTurn = 1
    OTurn = 2

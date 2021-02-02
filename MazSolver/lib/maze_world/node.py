import enum


class NodeStatus(enum.Enum):
    Normal = 0
    Start = 1
    Goal = 2
    InPath = 3


class NodeBorder:
    top: bool
    right: bool
    bottom: bool
    left: bool

    def __init__(self):
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False


class Node:
    row: int
    column: int
    status: NodeStatus
    border: NodeBorder

    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column
        self.border = NodeBorder()
        self.status = NodeStatus.Normal

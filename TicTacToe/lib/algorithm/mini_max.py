from lib.board.utilities import GameStatus, Node, NodeStatus
import math


class State:
    nodes: list[list[Node]]

    def __init__(self, nodes: list[list[Node]]):
        self.nodes = nodes


class MiniMaxAlphaBeta:
    board: list[list[Node]]
    game_statue: GameStatus

    def __init__(self, board: list[list[Node]], game_statue: GameStatus):
        self.board = board
        self.game_statue = game_statue

    def solve_problem(self) -> tuple[int, int]:
        state = State(self.board)
        if self.game_statue == GameStatus.XTurn:
            ((row, column), _) = self.maximizer(state, -math.inf, math.inf)
            return row, column
        elif self.game_statue == GameStatus.OTurn:
            ((row, column), _) = self.minimizer(state, -math.inf, math.inf)
            return row, column

    def maximizer(self, state: State, alpha: int, beta: int) -> tuple[tuple[int, int], int]:
        if self.terminal_state(state):
            return ((-1, -1), self.utility_function(state))
        v = -math.inf
        (row, column) = (-1, -1)
        for i in range(3):
            for j in range(3):
                if state.nodes[i][j].status == NodeStatus.Blank:
                    state.nodes[i][j].status = NodeStatus.X
                    new_state = State(state.nodes)
                    ((_, _), new_v) = self.minimizer(
                        new_state, alpha, beta)
                    state.nodes[i][j].status = NodeStatus.Blank
                    if new_v > v:
                        v = new_v
                        (row, column) = (i, j)
                    if new_v >= beta:
                        return((row, column), v)
                    alpha = max(alpha, new_v)
        return((row, column), v)

    def minimizer(self, state: State, alpha: int, beta: int) -> tuple[tuple[int, int], int]:
        if self.terminal_state(state):
            return ((-1, -1), self.utility_function(state))
        v = math.inf
        (row, column) = (-1, -1)
        for i in range(3):
            for j in range(3):
                if state.nodes[i][j].status == NodeStatus.Blank:
                    state.nodes[i][j].status = NodeStatus.O
                    new_state = State(state.nodes)
                    ((_, _), new_v) = self.maximizer(
                        new_state, alpha, beta)
                    state.nodes[i][j].status = NodeStatus.Blank
                    if new_v < v:
                        v = new_v
                        (row, column) = (i, j)
                    if new_v <= alpha:
                        return((row, column), v)
                    beta = min(beta, new_v)
        return((row, column), v)

    def terminal_state(self, state: State) -> bool:
        for i in range(3):
            # check rows
            if state.nodes[i][0].status == state.nodes[i][1].status == state.nodes[i][2].status != NodeStatus.Blank:
                return True
            # check columns
            if state.nodes[0][i].status == state.nodes[1][i].status == state.nodes[2][i].status != NodeStatus.Blank:
                return True

        # check diagonal
        if state.nodes[0][0].status == state.nodes[1][1].status == state.nodes[2][2].status != NodeStatus.Blank:
            return True
        if state.nodes[0][2].status == state.nodes[1][1].status == state.nodes[2][0].status != NodeStatus.Blank:
            return True

        for i in range(3):
            for j in range(3):
                if state.nodes[i][j].status == NodeStatus.Blank:
                    return False
        return True

    def utility_function(self, state: State) -> int:
        for i in range(3):
            # check rows
            if state.nodes[i][0].status == state.nodes[i][1].status == state.nodes[i][2].status != NodeStatus.Blank:
                if state.nodes[i][0].status == NodeStatus.X:
                    return 1
                else:
                    return -1
            # check columns
            if state.nodes[0][i].status == state.nodes[1][i].status == state.nodes[2][i].status != NodeStatus.Blank:
                if state.nodes[0][i].status == NodeStatus.X:
                    return 1
                else:
                    return -1

        # check diagonal
        if state.nodes[0][0].status == state.nodes[1][1].status == state.nodes[2][2].status != NodeStatus.Blank:
            if state.nodes[0][0].status == NodeStatus.X:
                return 1
            else:
                return -1
        if state.nodes[0][2].status == state.nodes[1][1].status == state.nodes[2][0].status != NodeStatus.Blank:
            if state.nodes[0][2].status == NodeStatus.X:
                return 1
            else:
                return -1

        return 0

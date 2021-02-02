from lib.chess_board.chess import Chess
import random
import math


class SA:
    chess: Chess
    T: float
    ratio: float

    def __init__(self, chess: Chess):
        self.chess = chess
        self.T = 1
        self.ratio = 0.05

    def random_init(self):
        self.chess.queens = [
            random.randint(1, self.chess.size) for _ in range(self.chess.size)]

    def evaluation_function(self):
        result = 0
        for i in range(self.chess.size):
            for j in range(i+1, self.chess.size):
                if self.chess.queens[i] == self.chess.queens[j]:
                    result += 1
                if abs(self.chess.queens[i] - self.chess.queens[j]) == j - i:
                    result += 1
        return result

    def queen_movment(self, column, new_row):
        self.chess.set_queen(new_row, column)

    def schedule_function(self) -> int:
        self.T = self.T-self.ratio
        if self.T < 0:
            self.T = 0
        return self.T

    def set_random_successor(self) -> tuple[int, int]:
        random_column = random.randint(1, self.chess.size)
        random_row = random.randint(1, self.chess.size-1)
        old_row = self.chess.queens[random_column-1]
        new_row = random_row if old_row > random_row else random_row+1
        self.queen_movment(random_column, new_row)
        return (random_column, old_row)

    def get_probability(self, DE, T) -> float:
        return math.exp(DE / T)

    def sovle_problem(self):
        self.random_init()

        while True:
            E1 = self.evaluation_function()
            if E1 == 0:
                return
            (column, old_row) = self.set_random_successor()
            E2 = self.evaluation_function()
            T = self.schedule_function()
            if E1-E2 > 0:
                continue
            elif T != 0:
                probability = self.get_probability(E1-E2, T)
                if random.random() > probability:
                    self.queen_movment(column, old_row)
            else:
                self.queen_movment(column, old_row)
                self.hill_climb()
                return

    def set_best_successor(self) -> bool:
        best_value = self.evaluation_function()
        column_changed = -1
        row_changed = -1
        for i in range(self.chess.size):
            for j in range(self.chess.size):
                old_row = self.chess.queens[i]
                self.queen_movment(i+1, j+1)
                value = self.evaluation_function()
                if value < best_value:
                    best_value = value
                    column_changed = i+1
                    row_changed = j+1
                self.queen_movment(i+1, old_row)
        if row_changed == -1:
            return False
        else:
            self.queen_movment(column_changed, row_changed)
            return True

    def hill_climb(self):
        while True:
            is_max = self.set_best_successor()
            if not is_max:
                break

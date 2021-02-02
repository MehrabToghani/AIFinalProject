class Chess:
    size: int
    queens: list[int]

    def __init__(self, size):
        self.size = size
        self.queens = [0 for _ in range(size)]

    def set_queen(self, row, column):
        self.queens[column-1] = row

    def print(self):
        result = ""
        for i in range(self.size):
            result += "------" * self.size + "-"
            result += "\r\n|"
            for j in range(self.size):
                if self.queens[j] == i+1:
                    result += "  X  |"
                else:
                    result += "     |"
            result += "\r\n"
        result += "------" * self.size + "-"
        print(result)

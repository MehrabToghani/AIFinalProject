from lib.board.utilities import GameStatus, Node, NodeStatus
from lib.algorithm.mini_max import MiniMaxAlphaBeta
import random
import tkinter
from tkinter import Label


class Board(tkinter.Frame):

    nodes: list[list[Node]]
    master: any
    game_status: GameStatus

    white = "#ffffff"
    dark_blue = "#1e1782"
    orange = "#e98c00"
    purple = "#ab0790"

    def __init__(self):
        self.nodes = [[Node(i+1, j+1) for j in range(3)] for i in range(3)]
        self.game_status = GameStatus.XTurn
        self.master = tkinter.Tk()
        super().__init__(self.master)
        self.master.title("Tic Tac Toe")
        self.master.geometry("400x300+400+200")
        self.home_screen()
        self.mainloop()

    def home_screen(self):
        frame = tkinter.Frame(self.master)
        frame.configure(bg=self.dark_blue)
        frame.place(width=400, height=300, x=0, y=0)

        welcome_label = tkinter.Label(
            master=frame, text="Welcome", bg=self.dark_blue, fg=self.white)
        welcome_label.config(font=("Arial", 20))
        welcome_label.place(y=20, width=400)

        tic_tac_toe_label = tkinter.Label(
            master=frame, text="Tic Tac Toe", bg=self.dark_blue, fg=self.white)
        tic_tac_toe_label.config(font=("Arial", 20))
        tic_tac_toe_label.place(y=80, width=400)

        def one_player_screen():
            frame.destroy()
            self.play_screen(is_tow_player=False)
        one_player = tkinter.Button(
            frame, text="1 Player", fg=self.white, bg=self.orange, command=one_player_screen)
        one_player.config(font=("Arial", 15))
        one_player.place(x=80, y=180, width=100)

        def two_player_screen():
            frame.destroy()
            self.play_screen(is_tow_player=True)

        two_player = tkinter.Button(
            frame, text="2 Players", fg=self.white, bg=self.orange, command=two_player_screen)
        two_player.config(font=("Arial", 15))
        two_player.place(x=220, y=180, width=100)

    def play_screen(self, is_tow_player: bool):
        frame = tkinter.Frame(self.master)
        frame.configure(bg=self.dark_blue)
        frame.place(width=400, height=300, x=0, y=0)

        def back():
            self.game_status = GameStatus.XTurn
            self.nodes = [[Node(i+1, j+1)
                           for j in range(3)] for i in range(3)]
            frame.destroy()
            self.home_screen()

        back_button = tkinter.Button(
            frame, text="Back", fg=self.white, bg=self.orange, relief="groove")
        back_button.config(font=("Arial", 10), command=back)
        back_button.place(x=20, y=20, width=50)

        is_x_bot: bool = False
        if not is_tow_player:
            if random.randint(1, 2) == 1:
                is_x_bot = True
            else:
                is_x_bot = False

        turn_label = tkinter.Label(
            master=frame, text="X turn" if is_tow_player else "You turn" if not is_x_bot else "Bot", bg=self.dark_blue, fg=self.white)
        turn_label.config(font=("Arial", 15))
        turn_label.place(y=20, x=100, width=200)

        boxes: list[list[Label]] = [[None for _ in range(3)]for _ in range(3)]

        def box_clicked(i, j):
            if 0 <= i <= 2 and 0 <= j <= 2 and self.nodes[i][j].status == NodeStatus.Blank:
                if self.game_status == GameStatus.XTurn:
                    boxes[i][j].config(text="X")
                    self.nodes[i][j].status = NodeStatus.X
                    turn_label.config(
                        text="O turn" if is_tow_player else "You turn" if is_x_bot else "Bot")
                    self.game_status = GameStatus.OTurn
                elif self.game_status == GameStatus.OTurn:
                    boxes[i][j].config(text="O")
                    self.nodes[i][j].status = NodeStatus.O
                    turn_label.config(
                        text="X turn" if is_tow_player else "You turn" if not is_x_bot else "Bot")
                    self.game_status = GameStatus.XTurn
                if self.check_win():
                    if self.game_status == GameStatus.OTurn:
                        turn_label.config(
                            text="X win!" if is_tow_player else "You win!" if not is_x_bot else "Bot win!")
                    elif self.game_status == GameStatus.XTurn:
                        turn_label.config(
                            text="O win!" if is_tow_player else "You win!" if is_x_bot else "Bot win!")
                    self.game_status = GameStatus.GameOver
                elif self.check_tie():
                    turn_label.config(text="Tie!")
                    self.game_status = GameStatus.GameOver
                if self.game_status == GameStatus.GameOver:
                    def restart():
                        self.game_status = GameStatus.XTurn
                        self.nodes = [[Node(i+1, j+1)
                                       for j in range(3)] for i in range(3)]
                        frame.destroy()
                        self.play_screen(is_tow_player)

                    restart = tkinter.Button(
                        frame, text="Restart", fg=self.white, bg=self.purple, command=restart)
                    restart.config(font=("Arial", 12))
                    restart.place(x=150, y=230, width=100)
                if not is_tow_player:
                    if (is_x_bot and self.game_status == GameStatus.XTurn) or \
                            (not is_x_bot and self.game_status == GameStatus.OTurn):
                        (i, j) = MiniMaxAlphaBeta(
                            self.nodes, self.game_status).solve_problem()
                        box_clicked(i, j)

        for i in range(3):
            for j in range(3):
                boxes[i][j] = tkinter.Button(
                    frame, text="", fg=self.white, bg=self.orange, relief="groove")
                boxes[i][j].config(
                    command=lambda i=i, j=j: box_clicked(i, j))
                boxes[i][j].config(font=("Arial", 30))
                boxes[i][j].place(x=125 + j*50, y=70+i*50, width=50, height=50)

        if is_x_bot and not is_tow_player:
            (i, j) = MiniMaxAlphaBeta(self.nodes, self.game_status).solve_problem()
            box_clicked(i, j)

    def check_win(self) -> bool:
        for i in range(3):
            # check rows
            if self.nodes[i][0].status == self.nodes[i][1].status == self.nodes[i][2].status != NodeStatus.Blank:
                return True
            # check columns
            if self.nodes[0][i].status == self.nodes[1][i].status == self.nodes[2][i].status != NodeStatus.Blank:
                return True

        # check diagonal
        if self.nodes[0][0].status == self.nodes[1][1].status == self.nodes[2][2].status != NodeStatus.Blank:
            return True
        if self.nodes[0][2].status == self.nodes[1][1].status == self.nodes[2][0].status != NodeStatus.Blank:
            return True

        return False

    def check_tie(self) -> bool:
        for i in range(3):
            for j in range(3):
                if self.nodes[i][j].status == NodeStatus.Blank:
                    return False
        return True

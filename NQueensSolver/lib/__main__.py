from lib.algorithm.sa import SA
from lib.chess_board.chess import Chess


if __name__ == '__main__':
    size = int(input("Enter number of Queens (size of board): "))
    print("--------------------------------------------------------------")

    chess = Chess(size)
    sa = SA(chess)
    sa.sovle_problem()

    chess.print()

    ef = sa.evaluation_function()
    if ef != 0:
        print("Evaluation Function = ", ef)
    else:
        print("Goal Found")
    print("--------------------------------------------------------------")

    while ef != 0:
        print("Goal not found. you can choose following options: ")
        print(" 1) Restart\r\n", "2) Sequential Restart\r\n", "3) Exit")
        option = int(input("Enter number of option: "))
        print("--------------------------------------------------------------")
        if option == 1:
            sa.sovle_problem()
            chess.print()
            ef = sa.evaluation_function()
            if ef != 0:
                print("Evaluation Function = ", ef)
            else:
                print("Goal Found")
            print("--------------------------------------------------------------")
        elif option == 2:
            number_of_restart = int(input("Enter Max Number of Restarts: "))
            print("--------------------------------------------------------------")
            for _ in range(number_of_restart):
                sa.sovle_problem()
                ef = sa.evaluation_function()
                if ef == 0:
                    break
            chess.print()
            ef = sa.evaluation_function()
            if ef != 0:
                print("Evaluation Function = ", ef)
            else:
                print("Goal Found")
            print("--------------------------------------------------------------")
        else:
            break

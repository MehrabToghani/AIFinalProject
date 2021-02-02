from lib.algorithm.a_star import AStar
from lib.maze_world.maze import Maze, WallDirection
from lib.maze_world.node import Node

if __name__ == '__main__':

    print("Options:\r\n", " 1) Default maze\r\n", " 2) Create custom maze")
    option = int(input("Enter number of option: "))

    print("\r\n--------------------------------------------------------------\r\n")
    if option == 1:
        maze = Maze(7, 8)

        maze.set_start(2, 1)
        maze.set_goal(6, 8)

        maze.set_wall(1, 8, WallDirection.Left)
        maze.set_wall(2, 8, WallDirection.Left)
        maze.set_wall(3, 8, WallDirection.Left)
        maze.set_wall(4, 8, WallDirection.Left)
        maze.set_wall(5, 8, WallDirection.Left)
        maze.set_wall(6, 8, WallDirection.Left)
        maze.set_wall(7, 7, WallDirection.Top)
        maze.set_wall(7, 6, WallDirection.Top)
        maze.set_wall(7, 5, WallDirection.Top)
        maze.set_wall(7, 3, WallDirection.Top)
        maze.set_wall(7, 3, WallDirection.Left)
        maze.set_wall(6, 4, WallDirection.Left)
        maze.set_wall(5, 4, WallDirection.Left)
        maze.set_wall(5, 4, WallDirection.Top)
        maze.set_wall(5, 5, WallDirection.Top)
        maze.set_wall(5, 6, WallDirection.Top)
        maze.set_wall(5, 6, WallDirection.Top)
        maze.set_wall(2, 1, WallDirection.Right)
        maze.set_wall(3, 1, WallDirection.Right)
        maze.set_wall(4, 1, WallDirection.Right)
        maze.set_wall(1, 2, WallDirection.Right)
        maze.set_wall(2, 2, WallDirection.Right)
        maze.set_wall(3, 2, WallDirection.Right)
        maze.set_wall(4, 2, WallDirection.Right)
        maze.set_wall(5, 2, WallDirection.Right)
        maze.set_wall(4, 3, WallDirection.Right)
        maze.set_wall(3, 3, WallDirection.Right)
        maze.set_wall(2, 3, WallDirection.Right)

        a_star = AStar(maze, Node(2, 1), Node(6, 8))
        cost = len(a_star.solve_problem())-1
        maze.print()
        if cost != -1:
            print("Cost:", cost)
        else:
            print("No solution path found!")

    elif option == 2:
        number_of_rows = int(input("Enter number of rows: "))
        number_of_columns = int(input("Enter number of columns: "))

        maze = Maze(number_of_rows, number_of_columns)

        while True:
            print("--------------------------------------------------------------")
            print("Options:\r\n", " 1) Show maze")
            print("  2) Add Start\r\n", " 3) Add Goal\r\n", " 4) Add Wall")
            print("  5) Remove wall\r\n", " 6) Solve\r\n", " 6) Exit")
            sub_option = int(input("Enter number of option: "))
            print(
                "--------------------------------------------------------------")

            if sub_option == 1:
                maze.print()
            elif sub_option == 2:
                print("Enter location of Start state in the form of: row column")
                (row, column) = input().strip().split(" ")
                row = int(row)
                column = int(column)
                maze.set_start(row, column)
            elif sub_option == 3:
                print("Enter location of Goal state in the form of: row column")
                (row, column) = input().strip().split(" ")
                maze.set_goal(int(row), int(column))
            elif sub_option == 4:
                print("Enter location of Wall in the form of: row column dir")
                print(" dir:\r\n  1) Top   2) Right   3) Bottom   4) Left")
                (row, column, dir) = input().strip().split(" ")
                maze.set_wall(int(row), int(column), WallDirection(int(dir)))
            elif sub_option == 5:
                print("Enter location of Wall in the form of: row column dir")
                print(" dir:\r\n  1) Top   2) Right   3) Bottom   4) Left")
                (row, column, dir) = input().strip().split(" ")
                maze.remove_wall(int(row), int(column),
                                 WallDirection(int(dir)))
            elif sub_option == 6:
                if maze.start and maze.goal:
                    a_star = AStar(maze, maze.start, maze.goal)
                    cost = len(a_star.solve_problem())-1
                    maze.print()
                    if cost != -1:
                        print("Cost:", cost)
                    else:
                        print("No solution path found!")
                    break
                else:
                    print("Please Specify Start and Goal State.")
            else:
                break

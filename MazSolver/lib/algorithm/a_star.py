from lib.algorithm.priority_queue import PriorityQueue, State
from lib.maze_world.maze import Maze
from lib.maze_world.node import Node, NodeStatus


class AStar:
    maze: Maze
    start: Node
    goal: Node
    pqueue: PriorityQueue

    def __init__(self, maze: Maze, start: Node, goal: Node):
        self.maze = maze
        self.maze.set_start(start.row, start.column)
        self.maze.set_goal(goal.row, goal.column)
        self.start = self.maze.nodes[start.row-1][start.column-1]
        self.goal = self.maze.nodes[goal.row-1][goal.column-1]
        self.pqueue = PriorityQueue()

    def get_successors(self, node: Node) -> list[Node]:
        successors = []
        if node.row != 1 and not node.border.top:
            successors.append(self.maze.nodes[node.row-2][node.column-1])
        if node.row != self.maze.number_of_rows and not node.border.bottom:
            successors.append(self.maze.nodes[node.row][node.column-1])
        if node.column != 1 and not node.border.left:
            successors.append(self.maze.nodes[node.row-1][node.column-2])
        if node.column != self.maze.number_of_columns and not node.border.right:
            successors.append(self.maze.nodes[node.row-1][node.column])
        return successors

    def manhattan_heuristic(self, node: Node) -> int:
        return abs(self.goal.row - node.row) + abs(self.goal.column - node.column)

    def is_goal(self, node: Node) -> bool:
        return self.manhattan_heuristic(node) == 0

    def evaluation_function(self, node, path_cost):
        return self.manhattan_heuristic(node) + path_cost

    def solve_problem(self) -> list[Node]:
        self.pqueue.add(
            State(self.start, None, self.evaluation_function(self.start, 0), 0))
        goal_state = None
        while not self.pqueue.empty():
            current = self.pqueue.get()
            if self.is_goal(current.node):
                goal_state = current
                break
            successors = self.get_successors(current.node)
            for successor in successors:
                self.pqueue.add(State(successor, current, self.evaluation_function(
                    successor, current.path_cost+1), current.path_cost+1))

        if goal_state is None:
            return []

        path = []
        current_node = goal_state
        while not current_node is None:
            if current_node.node.status == NodeStatus.Normal:
                current_node.node.status = NodeStatus.InPath
            path.append(current_node.node)
            current_node = current_node.parent

        return path

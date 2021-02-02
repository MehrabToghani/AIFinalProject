from lib.maze_world.node import Node
import heapq


class State:
    node: Node
    parent: "State"
    f_cost: int
    path_cost: int

    def __init__(self, node: Node, parent: "State", f_cost: int, path_cost):
        self.node = node
        self.parent = parent
        self.f_cost = f_cost
        self.path_cost = path_cost

    def __lt__(self, state: "State"):
        return self.f_cost < state.f_cost


class PriorityQueue:
    queue: list[State]

    def __init__(self):
        self.queue = []

    def empty(self) -> bool:
        return len(self.queue) == 0

    def add(self, state: State):
        # check is not cycle occured, Self ancestor
        current = state
        while current.parent:
            current = current.parent
            if state.node == current.node:
                return

        heapq.heappush(self.queue, state)

    def get(self) -> State:
        return heapq.heappop(self.queue)

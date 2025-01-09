from audioop import reverse
import copy
from re import T
from tkinter import N
import util
import random

class Node:

    def __init__(self, state, parent = None, real_value = 0, h_value = 0):
        self.state = state
        self.parent = parent
        self.real_value = real_value
        self.h_value = h_value

    def get_path(self):
        path = []
        current_node = self
        while current_node is not None:
            path.append(current_node.state)
            current_node = current_node.parent
        return path[::-1]

class Agent:

    def __init__(self):
        pass

    def _search(self, state, function, heuristic = None):
        start = Node(state)
        start.real_value = 0
        if heuristic is not None:
            start.h_value = heuristic(start.state)
        open = [start]
        closed = []
        count = 0
        while len(open) != 0:
            node = function(open)
            count += 1
            if node.state.is_goal():
                print(count,"\n")
                return node.get_path()
            closed.append(node)
            possible_actions = node.state.get_actions()
            for action in possible_actions:
                copy_node = copy.deepcopy(node)
                copy_node = Node(copy_node.state.execute(action))
                if copy_node.state not in [closed_node.state for closed_node in closed] and copy_node.state not in [open_node.state for open_node in open]:
                    new_node = Node(copy_node.state)
                    new_node.parent = node
                    new_node.real_value = node.real_value + 1
                    if heuristic is not None:
                        new_node.h_value = heuristic(new_node.state)
                    open.append(new_node)
            util.pprint(new_node.get_path())

    
    def pop_from_front(self, lst):
        return lst.pop(0)
    
    def pop_from_back(self, lst):
        return lst.pop()
    
    def sort_and_pop(self, lst):
        lst.sort(key=lambda node: node.real_value + node.h_value, reverse = True)
        return lst.pop(0)

    def BFS(self, state):
        return self._search(state, self.pop_from_front)

    def DFS(self, state):
        return self._search(state, self.pop_from_back)

    def a_star(self, state, heuristic):
        return self._search(state, self.sort_and_pop, heuristic)
    
    def random_walk(self, state, n = 8):
        previous_node = None
        current_node = Node(state)
        for i in range(1, n):
            possible_actions = current_node.state.get_actions()
            action = random.choice(possible_actions)
            previous_node = current_node
            current_node = Node(current_node.state.execute(action))
            current_node.parent = previous_node
        return current_node.get_path()
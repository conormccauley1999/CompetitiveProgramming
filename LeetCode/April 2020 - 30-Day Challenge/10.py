class Node:

    def __init__(self, x, m, n):
        self.v = x
        self.m = m
        self.n = n

class MinStack:

    def __init__(self):
        self.stack = None

    def push(self, x: int) -> None:
        if self.stack == None:
            self.stack = Node(x, x, None)
        else:
            cm = self.stack.m
            if x < cm: cm = x
            self.stack = Node(x, cm, self.stack)

    def pop(self) -> None:
        self.stack = self.stack.n

    def top(self) -> int:
        return self.stack.v

    def getMin(self) -> int:
        return self.stack.m

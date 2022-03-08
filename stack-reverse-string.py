from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)


string = "I Love Python"

stack = Stack()

for char in string:
    stack.push(char)

rev_string = ""
while stack.size() != 0:
    rev_string += stack.pop()

print(rev_string)

# nohtyP evoL I

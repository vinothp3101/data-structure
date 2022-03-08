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

def is_match(char):
    d = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    return d.get(stack.pop()) != char

def is_balanced(string):

    for char in string:
        if char in ["{", "[", "("]:
            stack.push(char)
        elif char in ["}", "]", ")"]:
            if stack.size() == 0:
                return False
            else:
                if is_match(char):
                    return False
        else:
            pass
    return stack.size() == 0


stack = Stack()

# value = input("enter values : ")  # "[{(1+3)}{2+3}{d+B}]")

# print(is_balanced(value))

print(is_balanced("[{(1+3)}{2+3}{d+B}]"))

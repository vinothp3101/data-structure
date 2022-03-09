from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def push(self, value):
        self.buffer.appendleft(value)

    def pop(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0


def place_order(orders):
    for order in orders:
        queue.push(order)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while not queue.is_empty():
        time.sleep(2)
        print(queue.pop())

queue = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

thread1 = threading.Thread(target=place_order, args=(orders,))
thread1.start()

thread2 = threading.Thread(target=serve_order, args=())
thread2.start()

########## output ########
# pizza
# samosa
# pasta
# biryani
# burger

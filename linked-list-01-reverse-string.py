class Node:
    def __init__(self, prev, data, next):
        self.prev = prev
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        if self.head is None:
            self.head = Node(None, value, None)
        else:
            next = self.head
            node = Node(None, value, next)
            next.prev = node
            self.head = node

    def print_backward(self):
        itr = self.head
        str = ""
        while itr:
            str += itr.data
            itr = itr.next
        print(str)

    def print_forward(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        str = ""
        while itr:
            str += itr.data
            itr = itr.prev
        print(f"{str}")

    def insert_values(self, list_value):
        for value in list_value:
            self.insert_at_beginning(value)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        print(f"Length of input is : {count}")

ll = LinkedList()
ll.get_length()
ll.insert_values("banana")
ll.print_backward()
ll.print_forward()

# output :
# ananab
# banana
# Length of input is : 6

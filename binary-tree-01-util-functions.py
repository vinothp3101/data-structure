class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data > self.data:
            if self.right is None:
                self.right = BinaryTree(data)
            else:
                self.right.add_child(data)

        if data < self.data:
            if self.left is None:
                self.left = BinaryTree(data)
            else:
                self.left.add_child(data)

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements

    def find_min(self):
        min = self.data
        if self.left:
            min = self.left.find_min()
        return min

    def find_max(self):
        max = self.data
        if self.right:
            max = self.right.find_max()
        return max

    def search(self, data):
        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return False

    def find_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.find_sum()
        if self.right:
            sum += self.right.find_sum()
        return sum

    def delete(self, data):
        if data == self.data:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max = self.left.find_max()
            self.data = max
            self.left = self.left.delete(max)

            # min = self.right.find_min()
            # self.data = min
            # self.right = self.right.delete(min)

        elif data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        else:
            if self.right:
                self.right = self.right.delete(data)

        return self

def build_binary_tree(elements):
    root = BinaryTree(elements[0])
    for i in elements:
        root.add_child(i)
    return root

if __name__ == "__main__":
    root = build_binary_tree([15, 12, 7, 14, 27, 20, 23, 88])
    print("in order traversal : ", root.in_order_traversal())
    print("pre order traversal : ", root.pre_order_traversal())
    print("post order traversal : ", root.post_order_traversal())
    print("min : ", root.find_min())
    print("max : ", root.find_max())
    print("sum : ", root.find_sum())
    print("search result : ", root.search(122))  # yes or no questions
    print("search result : ", root.search(12))  # yes or no questions
    root.delete(15)
    print("in order traversal : ", root.in_order_traversal())
    root.delete(277)
    print("in order traversal : ", root.in_order_traversal())

""" OUTPUT
in order traversal :  [7, 12, 14, 15, 20, 23, 27, 88]
pre order traversal :  [15, 12, 7, 14, 27, 20, 23, 88]
post order traversal :  [7, 14, 12, 23, 20, 88, 27, 15]
min :  7
max :  88
sum :  206
search result :  False
search result :  True
in order traversal :  [7, 12, 14, 20, 23, 27, 88]
in order traversal :  [7, 12, 14, 20, 23, 27, 88]

"""

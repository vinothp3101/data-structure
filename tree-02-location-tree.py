class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level):
        if self.get_level() > level:
            return

        spaces = " " * self.get_level() * 4
        prefix = f"{spaces}|__" if self.parent else ""
        print(f"{prefix}{self.data}")
        for child in self.children:
            child.print_tree(level)


def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    tamilnadu = TreeNode("Tamilnadu")
    chennai = TreeNode("Chennai")
    madurai = TreeNode("Madurai")
    karnataka = TreeNode("Karnataka")
    bengaluru = TreeNode("Bengaluru")
    mysore = TreeNode("Mysore")

    usa = TreeNode("USA")
    new_jersey = TreeNode("New Jersey")
    princeton = TreeNode("Princeton")
    trenton = TreeNode("Trenton")
    california = TreeNode("California")
    san_fransisco = TreeNode("San Fransisco")
    mountain_view = TreeNode("Mountain View")
    palo_alto = TreeNode("Palo Alto")

    root.add_child(india)
    root.add_child(usa)

    india.add_child(tamilnadu)
    india.add_child(karnataka)

    tamilnadu.add_child(chennai)
    tamilnadu.add_child(madurai)

    karnataka.add_child(bengaluru)
    karnataka.add_child(mysore)

    usa.add_child(new_jersey)
    usa.add_child(california)

    new_jersey.add_child(princeton)
    new_jersey.add_child(trenton)

    california.add_child(san_fransisco)
    california.add_child(mountain_view)
    california.add_child(palo_alto)

    return root

if __name__ == "__main__":
    root = build_location_tree()
    print("*"*50)
    root.print_tree(1)
    print("*"*50)
    root.print_tree(2)
    print("*"*50)
    root.print_tree(3)
    print("*"*50)


"""
**************************************************
Global
    |__India
    |__USA
**************************************************
Global
    |__India
        |__Tamilnadu
        |__Karnataka
    |__USA
        |__New Jersey
        |__California
**************************************************
Global
    |__India
        |__Tamilnadu
            |__Chennai
            |__Madurai
        |__Karnataka
            |__Bengaluru
            |__Mysore
    |__USA
        |__New Jersey
            |__Princeton
            |__Trenton
        |__California
            |__San Fransisco
            |__Mountain View
            |__Palo Alto
**************************************************
"""



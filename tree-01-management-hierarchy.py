class TreeNode:
    def __init__(self, designation, name):
        self.parent = None
        self.children = []
        self.designation = designation
        self.name = name

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

    def print_tree(self, format=None):
        level = self.get_level() * 4
        prefix = f"{' '*level}|__" if level else ""

        if format in ["designation", "name"]:
            print(f"{prefix} {getattr(self, format)}")
        else:
            print(f"{prefix} {self.name} ({self.designation})")

        for child in self.children:
            child.print_tree(format)

def build_management_tree():
    root = TreeNode("CEO", "A"*3)

    cto = TreeNode("CTO", "B"*3)
    hr_head = TreeNode("HR HEAD", "C"*3)

    infra_head = TreeNode("Infrastructure Head", "D"*3)
    app_head = TreeNode("Application Head", "E"*3)

    cloud_manager = TreeNode("Cloud Manager", "H"*3)
    app_manager = TreeNode("App Manager", "I"*3)

    recruitment_manager = TreeNode("Recruitment Manager", "F"*3)
    policy_manager = TreeNode("Policy Manager", "G"*3)

    root.add_child(cto)
    root.add_child(hr_head)

    cto.add_child(infra_head)
    cto.add_child(app_head)

    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)

    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)

    return root

if __name__ == "__main__":
    root = build_management_tree()
    print("*"*50)
    root.print_tree()
    print("*"*50)
    root.print_tree("designation")
    print("*"*50)
    root.print_tree("name")
    print("*"*50)

"""
OUTPUT:
**************************************************
 AAA (CEO)
    |__ BBB (CTO)
        |__ DDD (Infrastructure Head)
            |__ HHH (Cloud Manager)
            |__ III (App Manager)
        |__ EEE (Application Head)
    |__ CCC (HR HEAD)
        |__ FFF (Recruitment Manager)
        |__ GGG (Policy Manager)
**************************************************
 CEO
    |__ CTO
        |__ Infrastructure Head
            |__ Cloud Manager
            |__ App Manager
        |__ Application Head
    |__ HR HEAD
        |__ Recruitment Manager
        |__ Policy Manager
**************************************************
 AAA
    |__ BBB
        |__ DDD
            |__ HHH
            |__ III
        |__ EEE
    |__ CCC
        |__ FFF
        |__ GGG
**************************************************
"""

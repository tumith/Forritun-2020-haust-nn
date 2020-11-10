class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def insert(self,value,cur_node):
        if value < cur_node.value:     # if value is lower then node value
            if cur_node.left == None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node   # seting parent
            else:
                self.insert(value, cur_node.right)

        elif value > cur_node.value:  # if value is higher then node value
            if cur_node.right == None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node  # seting parent
            else:
                self.insert(value,cur_node.left)
        else:
            print('Value er núðegar í tréinu')

    def print_tree(self,cur_node):
        if cur_node != None:
            self.print_tree(cur_node.left)
            print(str(cur_node.value))
            self.print_tree(cur_node.right)
    
    def height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self.height(cur_node.left, cur_height + 1)
        right_height = self.height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)
    
    def search(self,value,cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self.search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self.search(value,cur_node.right_child)
        return False
    
    def find(self,value,cur_node):
        if value == cur_node:
            return cur_node
        elif value < cur_node.value and cur_node.left != None:
            return self.find(value,cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self.find(value,cur_node.right)


class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.insert(value,self.root)
    
    def print_tree(self):
        if self.root != None:
            self.root.print_tree(self.root)

    def height(self):
        if self.root != None:
            return self.root.height(self.root,0)
        else:
            return 0
    
    def search(self,value):
        if self.root != None:
            return self.root.search(value,self.root)
        else:
            return False

    def find(self,value):
        if self.root != None:
            return self.root.find(value,self.root)
        else:
            return None    



tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(1)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.print_tree()

print("tree height: " + str(tree.height()))

print(tree.search(7))

print(tree.find(3))
# https://github.com/bfaure/Python_Data_Structures/blob/master/Binary_Search_Tree/main.py
# https://www.youtube.com/watch?v=Zaf8EOVa72I&list=PLEJyjB1oGzx3iTZvOVedkT8nZ2cG105U7&index=6

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
        elif value < cur_node.value and cur_node.left != None:
            return self.search(value,cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self.search(value,cur_node.right)
        return False
    
    def find(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value<cur_node.value and cur_node.left!=None:
            return self.find(value,cur_node.left)
        elif value>cur_node.value and cur_node.right!=None:
            return self.find(value,cur_node.right)
        
    def delete_node(self,node):
        # Vernda gegn því að reina að eyða node sem finnst ekki
        if node == None or self.find(node.value) == None:
            print("Node sem var verið að reina að eyða fannst ekki")
            return None
        
        # skilar node með minsta value-ið
        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current
        
        def num_children(n):
            num_children = 0
            if n.left != None:
                num_children += 1
            if n.right != None:
                num_children += 1
            return num_children
        
        # ná í foreldrið af node-inu sem á að vera eitt
        node_parent = node.parent

        # numer af child-inu af node-inu sem á að vera eitt
        node_children = num_children(node)

        # break operation into different cases based on the
		# structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:

            # Added this if statement post-video, previously if you
            # deleted the root node it would delete entire tree
            if node_parent != None:
                #remove reference to the node from the parent
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None
        
        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left = None:
                child = node.left
            else:
                child = node.right

            # Adding this statement post-video, previously if you
            # deleted the root node it would delete entire tree.
            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child
            
            # correct the parent pointer in node
            child.parent = node_parent
        
        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)



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
        
    def delete_value(self, value):
        return self.root.delete_node(self.find(value))



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

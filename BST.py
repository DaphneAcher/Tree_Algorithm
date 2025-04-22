class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)

    #helper function to call easily
    def search(self, x):
        return self.search_tree(self.root, x)
    
    def search_tree(self,current,x):
        if self.root is not None:
            if current.value == x:
                return True
            elif current.value > x:
                return self.search_tree(current.left, x)
            else:
                return self.search_tree(current.right, x)
        else:
            return False
        
    # helper function to call easily    
    def delete(self, value):
        self.root = self.delete_node(self.root, value)

    def delete_node(self, current, value):
        if current is None:
            return None
        
        if value < current.value:
            current.left = self.delete_node(current.left, value)
        elif value > current.value:
            current.right = self.delete_node(current.right, value)
        else:
            # Case 1: no children
            if current.left is None and current.right is None:
                return None
            # Case 2: one child
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            # Case 3: 2wo children
            smallest = self.min(current.right)
            current.value = smallest.value
            current.right = self.delete_node(current.right, smallest.value)

        return current

    def min(self, node):
        while node.left:
            node = node.left
        return node
    
    #prints tree, research needed
    def print_tree(self):
        def print_(node, level=0):
            if node is not None:
                print_(node.right, level + 1)
                print('   ' * level + f'-> {node.value}')
                print_(node.left, level + 1)
        print_(self.root)





tree = BST()
for num in [8,3,1,6,4,7,10,14,13]:
    tree.insert(num)

tree.print_tree()

print(tree.search(6))

x = 4

tree.insert(x)

tree.print_tree()


tree.delete(6)
tree.print_tree()


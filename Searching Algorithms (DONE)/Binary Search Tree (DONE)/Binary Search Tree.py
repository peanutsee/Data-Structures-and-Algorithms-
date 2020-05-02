'''
Essentially the same as Trees......
Just copy and paste :P or make your own one to check your knowledge :P
'''

'''
Trees.... are quite complicated!

Idea is that, if the current value is greater than the new value, the new value goes to the left of the current value.
Opposite occurs if the new value is greater than the current value.
1. Values in Left Subtree is < Root
2. Values in Right Subtree is > Root

There are 3 ways of transversing a BST:

a. Depth First Transversals
1.In-Order: Left->Root->Right
2. Pre-Order: Root->Left->Right
3. Post-Order: Left->Right->Root

b. Breath First Transversals

BST Deletion Conditions
https://www.youtube.com/watch?v=gcULXE7ViZw
1. Node to be deleted is a leaf
2. Node to be deleted has only one child
3. Node to be deleted has 2 children
4. Node to be deleted is the root
'''

class Node():
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def __str__(self):
        return f'Data Value: {self.data}'

class Tree():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        if self.root == None:
            self.root = data
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if current.data == data.data: # Handles Duplicates
            return 'Duplicate values are not accepted.'
        elif current.data > data.data: # Handles when new data is smaller than current data (goes to the left)
            if current.left == None:
                current.left = data
            else:
                self._insert(current.left, data)
        else: # Handles when new data is smaller than current data (goes to the left)
            if current.right == None:
                current.right = data
            else:
                self._insert(current.right, data)

    def search(self, value_to_search):
        return self._search(self.root, value_to_search)

    def _search(self, current, value_to_search):
        if current:
            if current.data == value_to_search:
                return f'{value_to_search} found in tree.'
            else:
                if current.data > value_to_search:
                    return self._search(current.left, value_to_search)
                else:
                    return self._search(current.right, value_to_search)
        return f'{value_to_search} does not exist in tree.'

    def min_right_subtree(self, current):
        if current.left == None:
            return current
        else:
            return self.min_right_subtree(current.left)

    def delete(self, value_to_delete):
        self._delete(self.root, None, None, value_to_delete)

    def _delete(self, current, previous, is_left, value_to_delete):
        if current == None:
            return 'Tree is empty.'
        else:
            if current.data > value_to_delete: # Left Subtree
                return self._delete(current.left, current, True, value_to_delete)
            elif current.data < value_to_delete: # Right Subtree
                return self._delete(current.right, current, False, value_to_delete)
            else: # Value to Delete == Current
                if current.left and current.right:
                    min_child = self.min_right_subtree(current.right)
                    current.data = min_child.data
                    self._delete(current.right, current, False, min_child.data)
                elif current.left == None and current.right == None:
                    if previous:
                        if is_left:
                            previous.left = None # Removing leaf
                            #return f'{value_to_delete} has been deleted (Leaf Node)'
                        else:
                            previous.right = None # Removing lead
                            #return f'{value_to_delete} has been deleted (Leaf Node)'
                    else:
                        self.root = None # Root Removal
                        #return f'{value_to_delete} has been deleted (Root Node)'
                elif current.left == None and current.right:
                    if previous:
                        if is_left:
                            previous.left = current.right
                            #return f'{value_to_delete} has been deleted (Parent (kinda) Node)'
                        else:
                            previous.right = current.right
                            #return f'{value_to_delete} has been deleted (Parent (kinda) Node)'
                    else:
                        self.root = current.right
                        #return f'{value_to_delete} has been deleted (Root Node)'
                elif current.left and current.right == None:
                    if previous:
                        if is_left:
                            previous.left = current.left
                            #return f'{value_to_delete} has been deleted (Parent (kinda) Node)'
                        else:
                            previous.right = current.left
                            #return f'{value_to_delete} has been deleted (Parent (kinda) Node)'
                    else:
                        self.root = current.left
                        #return f'{value_to_delete} has been deleted (Root Node)'

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, curr):
        if not curr == None:
            self._in_order(curr.left)
            print(curr.data, end= " ")
            self._in_order(curr.right)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, curr):
        if not curr == None:
            print(curr.data, end= " ")
            self._pre_order(curr.left)
            self._pre_order(curr.right)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, curr):
        if not curr == None:
            self._post_order(curr.left)
            self._post_order(curr.right)
            print(curr.data, end= " ")

# Instantiate Tree
bst = Tree()

# Insert Values into Tree
bst.insert(5)
bst.insert(2)
bst.insert(12)
bst.insert(1)
bst.insert(3)
bst.insert(9)
bst.insert(21)
bst.insert(19)
bst.insert(25)
bst.insert(30)
bst.insert(24)

# Transversing Tree
bst.in_order()
print()
bst.pre_order()
print()
bst.post_order()

# Deletion
# Delete Root
bst.delete(5)

# Delete 1 Child
bst.delete(25)

# Delete 2 Child
bst.delete(21)

# Delete Lead
bst.delete(1)

print()
bst.in_order()













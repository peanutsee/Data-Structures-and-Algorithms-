'''
Similar to Queue, but this is LIFO.
Image playing with Matryoshka Doll. It is exactly that!

Python List
[] - Append()
[] - Pop()
'''

class Node():
    def __init__(self, data_value):
        self.data_value = data_value # Assign Data
        self.next = None # Initialize next as None

    def __str__(self):
        return f'Data Value: {self.data_value}'

class Stacks():
    def __init__(self):
        self.head = None

    def insert(self, data_to_insert): # Insertion idea is the same as Queue
        if not isinstance(data_to_insert, Node):
            data_to_insert = Node(data_to_insert)
        if self.head == None:
            self.head = data_to_insert
        else:
            data_to_insert.next = self.head
            self.head = data_to_insert

    def delete(self): # Always deletes the last element in the stack
        if self.head != None:
            self.head = self.head.next # Head assignment goes to the proceeding (preceding element, depends on how you see it)
            return 'Last node removed.'
        return 'Stack does not exist.'

    def peek(self): # Look at the top most value
        if self.head != None:
            return self.head
        return 'Stack does not exist.'

    def __str__(self):
        to_print = ''
        curr = self.head
        while not curr == None:
            to_print += str(curr.data_value) + "<-"
            curr = curr.next # Goes to next node of current node
        if to_print:
            return to_print[:-2]
        else:
            return 'Stack does not exist.'

# Instantiate Stack
stack = Stacks()

# Insert Values into Linked List
stack.insert("Vicki") # Insert to Head
stack.insert("Darryl") # Insert to Tail
stack.insert("Claudia") # Insert to Tail
stack.insert("Chan Jia Hui") # Insert to Head
stack.insert("Rachel") # Insert to Tail


# Print
print(stack.__str__())

# Deleting Node
print(stack.delete())
print(stack.__str__())

# Peek
print(stack.peek())

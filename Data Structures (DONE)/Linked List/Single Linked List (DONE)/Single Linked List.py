'''
Linear Data Structure: Linked List
1. Singly Linked List (Implement this first)
2. Doubly Linked List
3. Circular Linked List

Elements in the Linked List are linked using pointers, each node has a data value and a pointer that points to the next value.
'''

class Node():
    def __init__(self, data_value):
        self.data_value = data_value # Assign Data
        self.next = None # Initialize next as None

    def __str__(self):
        return f'Data Value: {self.data_value}'

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_to_tail(self, data_to_insert):
        # Check if data is a node type
        if not isinstance(data_to_insert, Node):
            data_to_insert = Node(data_to_insert)
        if self.head == None:
            self.head = data_to_insert
        else:
            self.tail.next = data_to_insert
        self.tail = data_to_insert # Ensure the newly inserted data is the tail

    def insert_to_head(self, data_to_insert):
        if not isinstance(data_to_insert, Node):
            data_to_insert = Node(data_to_insert)
        if self.head == None:
            self.head = data_to_insert
        else:
            data_to_insert.next = self.head # Shifts the current head to next of new head
            self.head = data_to_insert
        #self.tail = data_to_insert
        if self.tail == None:
            self.tail =  data_to_insert

    def index_node(self, data_to_search):
        if not self.head == None:
            curr = self.head
            n = 0
            while curr.data_value != data_to_search:
                curr = curr.next
                n += 1
            return f'Data {data_to_search} found at Index {n}.'
        return f'{data_to_search} does not exist in Linked List.'

    def delete_val_by_val(self, value_to_delete):
        # Keep track for current, prev and next
        curr = self.head
        prev = None

        while curr != None:
            if curr.data_value == value_to_delete:
                if prev != None:
                    prev.next = curr.next # curr not first element in linked list
                    return f'{value_to_delete} deleted from Linked List.'
                else:
                    self.head = curr.next # curr is first element in linked list
                    return f'{value_to_delete} deleted from Linked List.'
            else:
                prev = curr
                curr = curr.next
        return f'{value_to_delete} does not exist in Linked List.'

    def __str__(self):
        to_print = ''
        curr = self.head
        while not curr == None:
            to_print += str(curr.data_value) + "->"
            curr = curr.next # Goes to next node of current node
        if to_print:
            return to_print[:-2]
        else:
            return 'Linked List Does Not Exist'


# Instantiate Linked List
linked_list = LinkedList()

# Insert Values into Linked List
linked_list.insert_to_head("Vicki") # Insert to Head
linked_list.insert_to_tail("Darryl") # Insert to Tail
linked_list.insert_to_tail("Claudia") # Insert to Tail
linked_list.insert_to_head("Jia Hui") # Insert to Head
linked_list.insert_to_tail("Rachel") # Insert to Tail


# Print
print(linked_list.__str__())

# Searching for Node, return Index
print(linked_list.index_node('Darryl'))

# Deleting Node
print(linked_list.delete_val_by_val('Vicki'))
print(linked_list.__str__())

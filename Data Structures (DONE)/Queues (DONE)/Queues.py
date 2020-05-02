'''
Imagine aunties and uncles queuing up at NTUC to buy toilet paper
FIFO
'''

class Node():
    def __init__(self, data_value):
        self.data_value = data_value # Assign Data
        self.next = None # Initialize next as None

    def __str__(self):
        return f'Data Value: {self.data_value}'

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data_to_insert): # Always from the tail (FIFO, IDEA OF AUNTIES AND UNCLES RUSHING TO BUY TOILET PAPER)
        if not isinstance(data_to_insert, Node):
            data_to_insert = Node(data_to_insert)
        if self.head == None:
            self.head = data_to_insert
        else:
            self.tail.next = data_to_insert
        self.tail = data_to_insert

    def delete(self, value_to_delete): # Always from the left most (FIFO FIFO, IDEA OF AUNTIES AND UNCLES AT THE CASHIER PAYING FOR THE TOILET PAPER THEY BOUGHT)
        curr = self.head
        prev = None

        while curr != None:
            if curr.data_value == value_to_delete:
                if not curr == None:
                    if not prev == None:
                        prev.next = curr.next
                        return f'{value_to_delete} deleted from Queue.'
                    else:
                        self.head = curr.next
                        return f'{value_to_delete} deleted from Queue.'
            else:
                prev = curr
                curr = curr.next

        return f'{value_to_delete} does not exist in Queue.'

    def index_node(self, data_to_search):
        n = 0
        curr = self.head
        if curr:
            while curr.data_value != data_to_search:
                n += 1
                curr = curr.next
            return f'Data {data_to_search} found at Index {n}.'
        return f'{data_to_search} does not exist in Linked List.'

    def __str__(self):
        to_print = ''
        curr = self.head
        while not curr == None:
            to_print += str(curr.data_value) + "->"
            curr = curr.next # Goes to next node of current node
        if to_print:
            return to_print[:-2]
        else:
            return 'Queue does not exist.'

# Instantiate Queue
queue = Queue()

# Insert Values into Linked List
queue.insert("Vicki") # Insert to Head
queue.insert("Darryl") # Insert to Tail
queue.insert("Claudia") # Insert to Tail
queue.insert("Jia Hui") # Insert to Head
queue.insert("Rachel") # Insert to Tail


# Print
print(queue.__str__())

# Searching for Node, return Index
print(queue.index_node('Claudia'))

# Deleting Node
print(queue.delete('Vicki'))
print(queue.__str__())

class Node:
    '''
    An object for storing node of a linked list.
    Models 2 attributes - Data and link to the next node.
    '''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"<Node data: {self.data}>"

class LinkedList:
    '''
    Singly linked list.
    '''
    def __init__(self):
        self.head = None
    
    def check_if_empty(self):
        return self.head == None

    def size(self):
        '''
        Returns the number of nodes in the list.
        '''
        curr_node = self.head
        node_count = 0

        while curr_node:
            node_count += 1
            curr_node = curr_node.next_node
        
        return node_count
    
    def add_element(self, data):
        '''
        Add a new node containing data/element at the head of the list.
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search_element(self, search_elem):
        '''
        Search for the first node which contains data matching search_elem
        '''
        current = self.head

        while current:
            if current.data == search_elem:
                return current
            else:
                current = current.next_node
            
        return None

    def __repr__(self):
        '''
        String representation of the list.
        '''
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[ Head ] : {current.data}")
            elif current.next_node is None:
                nodes.append(f"{current.data} : [ Tail]")
            else:
                nodes.append(f"{current.data}")
            
            current = current.next_node
        return ' -> '.join(nodes)
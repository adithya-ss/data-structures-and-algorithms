from hashlib import new
from platform import node
from textwrap import indent


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
    
    def insert_new_node(self, data, pos):
        '''
        Inserts a new node containing data at given position.
        '''
        if pos == 0:
            self.add_element(data)
        
        if pos > 0:
            new_node = Node(data)
            curr_ind = pos
            current = self.head

        while curr_ind > 1:
            current = new_node.next_node 
            curr_ind -= 1
        
        prev_n = current
        next_n = current.next_node

        prev_n.next_node = new_node
        new_node.next_node = next_n
    
    def remove_node(self, del_elem):
        '''
        Delete a node from the linked list
        '''
        current = self.head
        prev_n = None
        node_found = False

        while current and not node_found:
            if current.data == del_elem and current is self.head:
                node_found = True
                self.head = current.next_node
            elif current.data == del_elem:
                node_found = True
                prev_n.next_node = current.next_node
            else:
                prev_n = current
                current = current.next_node

        return current

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
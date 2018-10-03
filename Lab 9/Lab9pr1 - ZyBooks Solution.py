'''
    Name: Peter Solimine
    Course: CMPS 1500
    Lab Section: Thursday 3:30 - 4:45pm 
    Assignment: Lab 9 pr 1
    Date: 04/17/2018
'''

class Node:
    def __init__(self, old = None, new = None, next = None):
        self.old = old
        self.new = new
        self.next = next

    def __eq__(self, other):
        return self.old == other.old and self.new == other.new

class LinkedList:
    def __init__(self, head=Node(), tail=Node()):
        self.head = head
        self.tail = tail

    def __contains__(self, node): #allows you to use '==' on two nodes
        temp = self.head
        empty_node = Node()
        #see if head exists
        if self.head == empty_node:
            return False
        #See if the first element of linked list is the same
        if temp == node:
            return True
        #check if any of the rest are the same
        while not temp == empty_node:
            if node == temp:
                return True
            temp = temp.next
        return False
    
    def add(self, newNode): #adds new node to linked list
        empty_node = Node()
        if self.head == empty_node:
            self.head = newNode
            self.tail = newNode
            newNode.next = empty_node
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = empty_node

    def remove(self, newNode): #removes node from list
        empty_node = Node()
        temp = self.head #Will be used only if the node is not the head
        if self.head == newNode:
            if self.head.next == empty_node: #Error here
                self.head = empty_node
                self.tail = empty_node
            else:
                self.head = self.head.next
                
        elif self.tail == newNode: #Though node can be both head and tail, This only runs if it is singularly the tail
            while not temp == empty_node:
                if temp.next == newNode:
                    self.tail = temp
                    temp.next = empty_node
                temp = temp.next
        else:
            while not temp == empty_node:
                if temp.next == newNode:
                    temp.next = temp.next.next
                temp = temp.next

    def findPerson(self, address):
        empty_node = Node()
        temp = self.head
        if temp == empty_node:
            return address
        while not temp == empty_node:
            if address == temp.old:
                address = temp.new
                temp = self.head          
            temp = temp.next
        return address

def add(old, new): 
    newNode = Node(old, new)
    if newNode in ForwardList:
        print('Entry already exists!')
    else:
        ForwardList.add(newNode)
        print('Added!')

def remove(old = None, new = None):
    newNode = Node(old, new)
    if newNode not in ForwardList:
        print('No such entry!')
    else:
        ForwardList.remove(newNode)
        print('Removed!')

def mail(address):
    print('Send to',ForwardList.findPerson(address))

       
ForwardList = LinkedList()
in_func = input()
while in_func.upper() != 'QUIT':
    if in_func.upper() == 'ADD':
        old = input()
        new = input()
        add(old, new)
        in_func = input()
    elif in_func.upper() == 'REMOVE':
        old = input()
        new = input()
        remove(old, new)
        in_func = input()
    elif in_func.upper() == 'MAIL':
        address = input()
        mail(address)
        in_func = input()

print('Goodbye') #when 'QUIT' is entered, loop exits, program terminates
        
        

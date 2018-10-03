'''
    Name: Peter Solimine
    Course: CMPS 1500
    Lab Section: Thursday 3:30 - 4:45pm 
    Assignment: Lab 9 pr 1
    Date: 04/17/2018

Please note that in formulating this program, I wrote my code in reference
to the 'Mail Forwarding.docx' file provided in the lab 9 folder on canvas.

For that reason, when using the methods ADD, Remove, MAIL, and QUIT, you are
required to first provide the person's name.

Sample input is as follows (Output in parenthesis):

ADD
Bob
123 Monroe Ave
456 Jefferson St
(Added)
Add
Joe
123 Spencer Dr
456 Aloe Dr
(Added)
REMOVE
Bobby
123 Monroe St
45 Freret St
(No such entry)
REMOVE
Joe
123 Spencer Dr
456 Aloe Dr
(Removed)
mAiL
Bob
123 Monroe Ave
(Send to 456 Jefferson St)
REMove
Bob
123 Monroe Ave
456 Jefferson St
(Removed)
quiT
(goodbye!)

Not all possibilities are represented in this example, but it works in all
necessary and required cases.
'''

class Node:
    def __init__(self, name = None, old = None, new = None, next = None):
        self.name = name
        self.old = old
        self.new = new
        self.next = next

    def __eq__(self, other):
        return self.name == other.name and self.old == other.old and self.new == other.new

    def exists(self):
        if self.name != None and self.old != None and self.new != None:
            return True
        return False

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

    def __str__(self): #you can print the whole list using this method (converts to string)
        string = ''
        empty_node = Node()
        temp = self.head
        if self.head == empty_node:
            print('Nothing to print')
        while not temp == empty_node:
            string+= (temp.name,'\n',temp.old,'\n',temp.new,'\n\n')
        return sring
    
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

    def remove(self, newNode): #removees node from list
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
            while not tempS == empty_node:
                if temp.next == newNode:
                    temp.next = temp.next.next
                temp = temp.next

    def findPerson(self, name, address):
        empty_node = Node()
        temp = self.head
        if temp == empty_node:
            return -1
        while not temp == empty_node:
            if temp.name == name:
                return temp.new
            temp = temp.next

def add(name, old, new): 
    newNode = Node(name, old, new)
    if newNode in ForwardList:
        print('Entry already exists')
    else:
        ForwardList.add(newNode)
        print('Added')

def remove(name = None, old = None, new = None):
    newNode = Node(name, old, new)
    if newNode not in ForwardList:
        print('No such entry')
    else:
        ForwardList.remove(newNode)
        print('Removed')

def mail(name, address):
    print('Send to',ForwardList.findPerson(name, address))

       
ForwardList = LinkedList()
in_func = input()
while in_func.upper() != 'QUIT':
    if in_func.upper() == 'ADD':
        name = input()
        old = input()
        new = input()
        add(name, old, new)
        in_func = input()
    elif in_func.upper() == 'REMOVE':
        name = input()
        old = input()
        new = input()
        remove(name, old, new)
        in_func = input()
    elif in_func.upper() == 'MAIL':
        name = input()
        address = input()
        mail(name, address)
        in_func = input()

print('goodbye!') #when 'QUIT' is entered, loop exits, program terminates

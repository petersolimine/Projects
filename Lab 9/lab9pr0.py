'''
    Name: Peter Solimine
    Course: CMPS 1500
    Lab Section: Thursday 3:30 - 4:45pm 
    Assignment: Lab 9 pr 0
    Date: 04/17/2018
'''

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def join(head1, head2):
    if head1 == None and head2 == None:
        return None
    elif head1 == None and head2 != None:
        return head2
    elif head1 != None and head2 == None:
        return head1
    temp = head1
    while temp.next != None:
        temp = temp.next
    temp.next = head2
    return head1
    
#Runtime is linear O(n) where n is the length of the list that begins with head1
    

    
'''
def ListAppend(list, newNode):
  if (list->head == null): // List empty
     list->head = newNode
     list->tail = newNode
  else:
     list->tail->next = newNode
     list->tail = newNode

def ListInsertAfter(list, curNode, newNode):
  if (list->head == null): // List empty
     list->head = newNode
     list->tail = newNode
  else if (curNode == list->tail): // Insert after tail
     list->tail->next = newNode
     list->tail = newNode
  else:
     newNode->next = curNode->next
     curNode->next = newNode
'''

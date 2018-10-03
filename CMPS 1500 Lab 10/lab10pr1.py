'''
    Name: Peter Solimine
    Course: CMPS 1500
    Lab Section: Thursday 3:30 - 4:45pm 
    Assignment: Lab 10 pr 1
    Date: 04/23/2018
'''
import sys
import time
class TreeNode:
    # this is how an object of our type will be initialized
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None

    # this function defines how to convert our type to a string
    def __str__(self):
        return str(self.data)

    # find a given element in a binary search tree
def tree_find(T, x):
    if (T == None):
        return False
    elif (T.data == x):
        return True
    elif (x <= T.data  ):
        return tree_find(T.left, x)
    else:
        return tree_find(T.right, x)

# insert a new item into a binary search tree
def tree_insert(T, x):
    
    # this is to build a new tree, essentially create a root node
    if (T == None):
        return TreeNode(x)
        # if the tree has something in it already, then insert x
    if (x >= T.data):
        if (T.right == None):
            T.right = TreeNode(x)
        else:
            tree_insert(T.right, x)
    elif (x < T.data ):
        if (T.left == None):
            T.left = TreeNode(x)
        else:
            tree_insert(T.left, x)

f = open('wordlist.txt', 'r')
# L contains the list of words in word_list.txt
L = f.read().split()
sys.setrecursionlimit(len(L))
T = tree_insert(None, L[0])
#create a root node
#change 1 to be 2, 10, etc to generate lists of different length
# construct a binary tree from the given word list
# adding each item of L into a new binary tree
# add code to measure time to add elements
for n in range(0, 1000, 25):
    for i in range(1, n):
        tree_insert(T, L[n-i])
    initial_time = time.clock()
    for j in range(0, 500):
        tree_find(T, "John") #word will not be found so it will check full tree
        j+=1
    after_time = time.clock()
    diff = after_time-initial_time
    print('The program took ',diff,'seconds to check the full BST of containing',n,'items 500 times.')
# now peform a series of experiments: pick a random element in the list and search for it in the tree.
# record the times it takes, and observe how the time depends on different values of n

'''
    Name: Peter Solimine
    Course: CMPS 1500
    Lab Section: Thursday 3:30 - 4:45pm 
    Assignment: Lab 10 pr 0
    Date: 04/23/2018
'''

class TreeNode:
    def __init__(self,data=None, right = None, left = None):
        self.data = data
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.data)

#include your getheight function here
def getheight(root):
    if type(root) is not TreeNode:
        return 0
    elif type(root.right) is not TreeNode or type(root.left) is not TreeNode:
        return 0
    else:
        return getheight(root.left)+1

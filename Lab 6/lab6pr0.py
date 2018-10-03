"""
Name: Peter Solimine
Course: CMPS 1500
Lab Section: Thursday 3:30-4:45pm 
Assignment: Lab 6
Date: 03/21/2018
"""

def is_sorted(lst):
    '''
    Determines whether the list is sorted in ascending order.
    Args:
        lst (List): given list of numbers
    Returns:
        True if sorted
    '''
    list_len = len(lst)-1
    for i in range(list_len): 
        if lst[i] > lst[i + 1]:
            return False
    return True

def is_file_sorted(filename):
    '''
    Finds if data in file is sorted
    Args:
        filename (str): file of numbers each number is on a new line.
    returns:
        true if sorted
    '''
    f = open(filename, 'r')
    txt = f.readlines()
    lines = []
    f.close()
    for i in range(len(txt)-1):
        lines.append(int(txt[i]))
    return is_sorted(lines)

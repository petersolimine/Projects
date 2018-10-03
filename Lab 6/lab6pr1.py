"""
Name: Peter Solimine
Course: CMPS 1500
Lab Section: Thursday 3:30-4:45pm 
Assignment: Lab 6 Pr 1
Date: 03/21/2018
"""

def is_sorted(lst):              #O(1)
    '''
    Determines whether the list is sorted in ascending order.
    Args:
        lst (List): given list of numbers
    Returns:
        True if sorted
    '''
    list_len = len(lst)-1         #O(1)
    for i in range(list_len):     #O(n)
        if lst[i] > lst[i + 1]:   #O(1)
            return False          #O(1)
    return True                   #O(1)

def is_file_sorted(filename):     #O(1)
    '''
    Finds if data in file is sorted
    Args:
        filename (str): file of numbers each number is on a new line.
    returns:
        true if sorted
    '''
    f = open(filename, 'r')       #O(1)
    txt = f.readlines()           #O(1)
    lines = []                    #O(1)
    f.close()                     #O(1)
    for i in range(len(txt)-1):   #O(n)
        lines.append(int(txt[i])) #O(1)
    return is_sorted(lines)       #O(1)

def main():
    '''
    prints whether or not the file is sorted.
    args:
        filename (str): name of file 
    returns:
        none
    '''
    filename = print('Please enter file name: ')              #O(1)

    if is_file_sorted(filename) == True:                      #O(1)
        print('Congratulations! The file ', filename, ' is nicely sorted!') #O(1)
    else:                                                     #O(1)
        print('Looks like ', filename, ' needs to be sorted') #O(1)

'''Final runtime is O(n) because that is the highest level complexity of O(n) seen in the program'''

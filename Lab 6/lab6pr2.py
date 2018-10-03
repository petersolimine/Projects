'''
  Peter Solimine
  CMPS 1500
  Thursday 3:30-4:45
  Lab 6 Part 2
  03/21/2018
'''

import random
random.seed(0)

 
def selection_sort( aList ):
  """Sorts a list in ascending order using the selection sort algorithm.
  """
  n = len( aList )
  for i in range( n - 1 ):
    
      
    # Find the minimum element in the unsorted portion of the list
    
    smallNdx = i # assume the ith element is the smallest.
    
    # Determine if any other element contains a smaller value.
    for j in range( i + 1, n ):
      if aList[ j ] < aList[ smallNdx ] :
        smallNdx = j

    # Swap the ith value and smallNdx value  
                      
    tmp = aList[ i ]
    aList[ i ] = aList[ smallNdx ]
    aList[ smallNdx ] = tmp

  return aList  


def merge_sort( aList ):
    """
    Merge sort recursively divide the list into half, sort both halves
    and then merge the two sorted lists into one.
    """
    # If the aList is size 0 or 1, it's already sorted.
    if len( aList ) <= 1:
        return aList

    else:
        mid = len( aList ) // 2

        # Recursively sort the left and right halves
        left = merge_sort( aList[ :mid ] )
        right = merge_sort( aList[mid:] )
        
        # Merge the two (each sorted) parts back together
        return merge( left, right )


                                
def merge( left, right ):
    """
    Merge to sorted list, left and right, into one sorted list.
    """
    aList = []
    lt = 0
    rt = 0

    # Repeatedly move the smallest of left and right to the new list
    while lt < len( left ) and rt < len( right ):
        if left[ lt ] < right[ rt ]:
            aList.append( left[ lt ]  )
            lt += 1
        else:
            aList.append( right[ rt ] )
            rt += 1

    # There will only be elements left in one of the original two lists.

    # Append the remains of left (lt..end) on to the new list.
    while lt < len(left):
        aList.append( left[ lt ] )
        lt += 1
         
    # Append the remains of right (rt..end) on to the new list.
    while rt < len( right ):
        aList.append( right[ rt ] )
        rt += 1

    return aList

def use_mergesort(inputfile, outputfile):
    '''
      Takes an input file uses mergesort to create new, sorted file
    Args:
        input (str): Input file with list of integers
    Returns:
        None
    '''
    f = open(inputfile, 'r')
    text = f.read()
    f.close
    
    num_lst = text.split()
    str_len = len(num_lst)
    for i in range(str_len):
        num_lst[i] = int(num_lst[i])
        
    sorted_lst = merge_sort(num_lst)
    output = ''
    for i in range(len(num_lst)):
        output += str(sorted_lst[i])
        output += '\n'
        
    k = open(outputfile, 'w')
    k.write(output)
    k.close()
    return

def use_selection(inputfile, outputfile):
    '''
      input file of ints and use selection sort to create a new, sorted file.
    Args:
        inputfile (str): Input file with list of integers
        outputfile (str): filename for new sorted list
    Returns:
        None
    '''
    f = open(inputfile, 'r')
    text = f.read()
    f.close
    
    num_lst = text.split()
    str_len = len(num_lst)
    for i in range(str_len):
        num_lst[i] = int(num_lst[i])
    selection_sort(num_lst)
    output = ''
    for i in range(len(num_lst)):
        output += str(num_lst[i])
        output += '\n'
        
    k = open(outputfile, 'w')
    k.write(output)
    k.close()
    return

def generate_nums(filename, n):
    '''
      Writes n number of random nums from 0-99 to file
    Args:
        filename (str): Output filename
        n (int): # of random ints to generate
    Returns:
        None
    '''
    output = ''
    for i in range(n):
        num = random.randrange(0, 100)
        output += str(num)
        output += '\n'

    f = open(filename, 'w')
    f.write(output)
    f.close()
    return

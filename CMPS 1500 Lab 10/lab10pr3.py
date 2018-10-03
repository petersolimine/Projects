'''
    Name: Peter Solimine
    Course: CMPS 1500
    Lab Section: Thursday 3:30 - 4:45pm 
    Assignment: Lab 10 pr 3
    Date: 04/25/2018
'''

def isClique(G, X, k):
    #method tests given group of vertices to see if they make up a 'clique'
    counter=0
    if G == {}:
        return False
    if len(X) == k: #must be false otherwise
        
        for first in X:
            for runner in X:
                if first != runner:
                    if first not in G[runner] and runner not in G[first]:
                        return False
            return True
    return False

#the runtim ein Big Oh form is O(n squared) where 'n' is the length of x
#This is because there are nested forloops which iterate n times each,
#assuming n is the length of X.
#can be checked in polynomial time at most so it is an NP problem

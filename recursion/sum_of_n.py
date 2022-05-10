import sys
sys.setrecursionlimit(2000) 
def sum (n):
    if (n == 1): 
        return 1
    else:
        return n + sum(n-1)

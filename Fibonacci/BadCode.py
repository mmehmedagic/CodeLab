"""
21/10/2019:
Given input integer n, calculate the Fibonacci sequence up to index n, lists 0 indexes of course.
--------
Bad Code (actual entry)
54 characters
"""
n = int(input("Index? "))  # Not counted
l=[0]  # Counted
if n>0:l+=[1]  # Counted
for x in range(n-1):l+=[l[x]+l[x+1]]  # Counted
print(l[-1])  # Not counted

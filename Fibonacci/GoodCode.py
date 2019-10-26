"""
21/10/2019:
Given input integer n, calculate the Fibonacci sequence up to index n, lists 0 indexes of course.
--------
Good Code (readable)
"""

def fibonacci(num, lst=[]):
    lst.append(0)
    if num > 0:
        lst.append(1)
    for x in range(num - 1):
        lst.append(lst[x] + lst[x + 1])
    print(lst[-1])


fibonacci(10)

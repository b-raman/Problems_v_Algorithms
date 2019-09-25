#!/usr/bin/env python
# coding: utf-8

# In[16]:


"""
Bharat Raman: problem 6
finding the min and max in an unsorted array

time complexity: O(n). using a for loop for single traversal 
space complexity: O(1). Array created outside of function. Inside of function, only two ints are declared
"""

def get_min_max(ints): #O(n) in a single traversal
    if len(ints) == 0:
        print("ERROR: Empty array")
        return None
    #initialized min and max to be the first element of the array
    minimum = ints[0]
    maximum = ints[0]
    for i in ints: #in a for loop, look for any integer that surpasses the current min and max. update accordingly
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    return (minimum,maximum) #return min and max as a tuple

## Example Test Case of Ten Integers
import random

"""
Test 1: numbers -50 to 99
expected output:
    (-50, 99)
"""
l = [i for i in range(-50, 100)]  # a list containing 0 - 9
random.shuffle(l)
print (get_min_max(l))

"""
Test 2:an array of strings
expected output:
    ('aoli', 'zebra')
"""
print (get_min_max(['bannana', 'aoli', 'fungi', 'zebra', 'maple']))

"""
Test 3:(edge case) an empty array
expected output:
    ERROR: Empty array
    None
"""
print (get_min_max([]))

"""
Test 4:(edge case) an array with one element
expected output:
    (8, 8)
"""
print (get_min_max([8]))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Bharat Raman: Problem 1
#using a binary search here, with a run-time of O(log(n))


def sqrt(number):
    if number < 0: #if the input is a negative number, make sure output is imaginary
        return str(sqrt(abs(number))) + ' * i'
        
    if number == 0 or number == 1:
        return number
    search_range = number//2 #using a number instead of an array for binary search. Avoids O(n) complexity
    return(binary_search(search_range,number))

#binary search method modified from lessons. Looks at the square of the mid instead of the mid iteself
#instead of using an array, it uses a reference range, that will truncate via traditional binary search
def binary_search(search_range, target):
    start_index = 0
    end_index = search_range
    
    while start_index <= end_index:
        mid = (start_index + end_index)//2        # integer division in Python 3
        square = mid**2
        if square == target:     # we have found the element
            return mid
        elif target < square:                      # the target is less than the mid
            end_index = mid - 1                   # we will only search in the left half
        
        else:                                           # the target is greater than the mid
            start_index = mid + 1               # we will search only in the right half
    
    #if perfect square was not found, mid_index would have reached the closest integer to sqrt(target)
    if mid**2 > target: #check if closest integer squared is greater than target
        return mid - 1  #if so, subtract by one to reach the floor value
    return mid 

#Tests

"""
Test 1: sqrt(9)
expected output: 3
"""

print (sqrt(9))

"""
Test 2: (edge case) negative number
expected output: 4 * i
"""
print (sqrt(-16))

"""
Test 3: zero
expected output: 0
"""
print(sqrt(0))

"""
Test 4: (edge case) closest integer to sqrt(imperfect square)
expected output: 5
"""
print (sqrt(35))


# In[ ]:





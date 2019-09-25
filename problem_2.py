#!/usr/bin/env python
# coding: utf-8

# In[4]:


"""
Bharat Raman: Problem 2
Rotated array search
Uses two versions of binary search, both of runtime O(logn)
Part 1 uses binary search to identify where the pivot of rotation is
Part 2 is a typical binary search, except the start and end indeces are specified as arguments
    these arguments are used so that, depending on the value of the number, it can focus on the lower or upper portion of array
"""
def rotated_array_search(arr, number):
    if len(arr) == 0:
        print("ERROR: Array is empty")
        return -1
    #Part 1. Find where the sorted array begins using binary search: O(logn)
    start_index = 0
    end_index = len(arr) - 1
    arr_end = arr[end_index]
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2
        mid = arr[mid_index]
        if mid > arr_end:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1
    
    #Part 2: depending on the value of target, do a binary search from either the rotated portion, or original portion: O(logn)
    if number >= arr[0]:
        return binary_search(arr,0,start_index-1,number)
    else:
        return binary_search(arr,start_index, len(arr)-1, number)

def binary_search(array, start, end, target):
    start_index = start
    end_index = end
    while start_index <= end_index:
        mid_index = (start_index + end_index)//2
        mid = array[mid_index]
        if target == mid:                       
            return mid_index
        elif target < mid:                      
            end_index = mid_index - 1                   
        else:                                           
            start_index = mid_index + 1         
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    output = rotated_array_search(input_list, number)
    print(output)
    if linear_search(input_list, number) == output:
        print("Pass\n")
    else:
        print("Fail\n")

#Tests
"""
Test 1: at index 3
Expected output:
    7
    Pass
"""
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 3])

"""
Test 2: (edge case) item not in array
Expected output:
    -1
    Pass
"""
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

"""
Test 3: (edge case) empty array
Expected output:
    ERROR: Array is empty
    -1
    Pass
"""
test_function([[], 1])


# In[ ]:





# In[ ]:





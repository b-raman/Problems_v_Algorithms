#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
Bharat Raman: problem 4
Sorting 0's, 1's, 2's in a single traversal (O(n))
Using a while loop, and keeping track of zero's/two's indices, swap as cursor progresses to twos_index
"""

def sort_012(input_list): #O(n)
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_index = 0
    twos_index = len(input_list) - 1
    cursor = 0
    while cursor <=twos_index:
        #check if input_list at cursor is a valid term (0,1,2) 
        #Otherwise, return None since the input is beyond scope of algorithm
        if input_list[cursor] != 0 and input_list[cursor] != 1 and input_list[cursor] != 2:
            print("ERROR: invalid term(s) present in array")
            return None
        
        if zero_index > cursor: #check if zero index has exceeded cursor. if so, set cursor = 0 index
            cursor = zero_index
        
        elif input_list[cursor] == 0: ####if it's a 0####
            if input_list[zero_index] != 0: #swap with what's currently at zero_index if that's not 0
                input_list = swap_values(input_list,cursor,zero_index)
                cursor += 1 #only increment cursor if swap happens. Otherwise, wait for next iteration to check next index
            zero_index += 1
        
        elif input_list[cursor] == 2: ####if it's a 2####
            if input_list[twos_index] == 0: #special case: swap with element at zero_index. then wait for next iteration
                input_list = swap_values(input_list,twos_index,zero_index)
                zero_index += 1 #increment 0 index since a 0 has been pushed here
            else:
                if input_list[twos_index] == 1: #if not a 0, then swap accordingly, just like before, but with 2's index
                    input_list = swap_values(input_list,cursor,twos_index)
                    cursor += 1
                twos_index -= 1 #decrement 2's index since a 2 has been pushed there
        else: ####otherwise, continue on. 1's will fall in place as 0's and 2's are sorted####
            cursor += 1
    return input_list

def swap_values(arr, index1, index2): #O(1) helper method for swapping values in an array
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass\n")
    else:
        print("Fail\n")

"""
Test 1: unsorted array
expected output:
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    Pass
"""
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
"""
Test 2: pre-sorted array
expected output:
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    Pass
"""
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

"""
Test 3: (edge case) array with an invalid term
expected output:
    ERROR: invalid term(s) present in array
    None
    Fail
"""
test_function([2, -1, 3, 0, 1, 5, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 1])

"""
Test 4: (edge case) array with only 0's
expected output:
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Pass
"""
test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


# In[ ]:





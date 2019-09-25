#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Bharat Raman: Problem 3
finding two numbers, whose digits are comprised of those in an array, that have the largest sum (O(n + nlogn) = O(nlogn))
Step 1: O(nlogn): sort the input array using merge sort (implementation from lesson)
Step 2: O(n): use a for loop, from largest number to smallest, and keep updating two different numbers in alternate fassion. 
"""
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    #step 1: sort array via merge sort (O(nlogn))
    sorted_arr = mergesort(input_list)
    
    #in a for loop, (O(n)), find two largest numbers to make largest sum
    nums = [0,0]
    left = True
    for i in range(len(sorted_arr)-1,-1,-1):
        if left:
            n = nums[0]
            nums[0] = n*10 + sorted_arr[i]
            left = False
        else:
            n = nums[1]
            nums[1] = n*10 + sorted_arr[i]
            left = True
    return nums
    pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass\n")
    else:
        print("Fail\n")

#Tests
"""
Test 1: sorted array
Expected output:
    [531, 42]
    Pass
"""
test_function([[1, 2, 3, 4, 5], [542, 31]])

"""
Test 2: unsorted array
Expected output:
    [964, 852]
    Pass
"""
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

"""
Test 3: (Edge case) Array with two elements
Expected output:
    [2, 1]
    Pass
"""
test_function([[1, 2], [1, 2]])

"""
Test 4: (Edge case) Empty Array
Expected output:
    [0, 0]
    Pass
"""
test_function([[], []])


# In[ ]:





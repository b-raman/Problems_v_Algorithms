Bharat Raman
Problem 3: Find largest sum of numbers whose digits come from an unsorted array

    Time complexity: O(nlogn) = (O(n + nlog(n))
        O(n) from a for loop, and O(nlogn) from merge-sort algorithm
    Space complexity: O(n)
        auxiliary space complexity for merge-sort algorithm

For this problem, I started by sorting the array using merge sort, whose time complexity is O(nlogn).
    So [4, 6, 2, 5, 9, 8]  -> merge-sort  ->  [2, 4, 5, 6, 8, 9]
    
Once sorted, I used a for-loop (O(n)) to create the two numbers whose sum is the maximum possible.
For generating the sums, I had an array nums = [0,0]
Then, in the for-loop, starting from the end-index and decrementing by 1, I appended alternatively, to each index of nums, the numbers in input list
    [2, 4, 5, 6, 8, 9] -> for-loop ->  [964, 852]

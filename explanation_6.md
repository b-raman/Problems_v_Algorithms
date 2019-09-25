Bharat Raman
Problem 6: Finding the min/max, in a single traversal, of an array

    Time complexity: O(n)
        for loop navigating through array in one traversal
    Space Complexity: O(1)
        array passed as an argument for problem. nothing is being created iteratively

For this problem, I used a for-loop to navigate from start to finish. The min and max were initialized as the first element of the array. During the loop, if a number was smaller than the min, then the min would be updated. If a number was bigger than the max, then the max would be updated. The result is a tuple for the array’s minimum and maximum values

Bharat Raman
Problem 1: Finding the square root (floor) of a target

    Time complexity: O(logn)
        This is the time complexity of a binary search
    Space complexity: O(1)
        Nothing is being created iteratively

For this problem, I implemented a binary search, since its worst-case time complexity is O(logn). Though quite similar to the standard binary search, a change I made was to not use an array for searching, but a number. This way, I’ve avoided any O(n) operations in creating the array.

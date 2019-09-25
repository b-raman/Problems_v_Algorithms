Bharat Raman
Problem 2: Rotated array search

    Time complexity: O(logn)
        I’m using two seperate binary searches, both of which are O(logn)
    Space complexity: O(1)
        array is passed as an argument, and nothing is being created iteratively

My solution to this problem is separated into two binary searches. The first binary search looks for the point where the sorted array is supposed to start. Once that is found, the second part looks for the index of the target within the numbers past (and including) the 0th term, or the numbers before. Both binary searches are separately executed and are of complexity O(logn)

Bharat Raman
Problem 4: Sorting 0’s 1’s and 2’s in a single traversal

    Time Complexity: O(n)
        n >= length of array since i (in n) does not increment every iteration
    Space complexity: O(1)
        values in array are only being swapped. Array itself is passed as an argument for the problem

For this problem, I implemented a while-loop that navigates the input_list with a cursor. Looking at each number, the code keeps track of the 0’s and 2’s index, and swaps around values at cursor with values at the other indices. Once the cursor has reached the end of the list. It’s safe to say that the list has been sorted.
    Note. If the value at cursor is 2, there is a special case for if the value at 2’s index is 0. Since cursor is past the 0’s index, two swaps need to happen. One with the 2’s index and 0’s index, and one with the 2’s index and cursor. Please look at code for more details

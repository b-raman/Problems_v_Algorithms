Bharat Raman
Problem 7: Router, using a Trie

    Time complexity: O(n*m)
        n is the number of levels in the tree, and m is the number of nodes per level
    Space complexity: O(n*m)
        for each level, n, in the trie, m nodes are being created

This problem takes many elements from problem 5. The main difference here is that the nodes store a handler string instead of a boolean for whether a word was found. Aside from that, the other noticeable difference is that, instead of containing a character dictionary, the trie nodes contain sub-directory dictionaries.

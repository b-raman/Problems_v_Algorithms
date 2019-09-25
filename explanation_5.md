Bharat Raman
Problem 5: Finding Suffixes with Tries

    Time Complexity: O(n*m)
        n is the number of suffixes for the inputted prefix, and m is the number of words per suffix
    Space Complexity: O(n*m)
        n is the number of words, m is the length of the word. In total, there will be n*m Trie-nodes

For this problem, I implemented a Trie based off the Trie (from the lessons) used to check if a word exists, or not. This one differs in that it now looks for all suffixes that, combined with the prefix, make an existing word in the Trie. The method that finds all suffixes is a recursive method in the class TrieNode. It returns an array of all suffixes under that node.

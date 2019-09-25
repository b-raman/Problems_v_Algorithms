#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Bharat Raman: Problem 5
From notebook on Tries
"""
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        node_suffixes = []
        if self.is_word: #
            if self.children == {}:
                return []
            else:
                node_suffixes.append(suffix)
        
        
        for char in self.children:
            child_suffixes = self.children[char].suffixes(char)
            if len(child_suffixes) == 0:
                node_suffixes.append(suffix + char)
            else:
                for s in child_suffixes:
                    node_suffixes.append(suffix + s)
        return node_suffixes
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        currentNode = self.root #start at root
        for char in word: #for each character, navigate down trie, and make new nodes as appropriate
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.is_word = True #At end of for loop, have reached the last TrieNode for the word

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        currentNode = self.root
        for char in prefix:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return None
        return currentNode
    
#Testing    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            return('\n'.join(prefixNode.suffixes()) + '\n')
        else:
            return("Error: '" + prefix + "' not found\n")
    else:
        return('NaN\n')

#Testing
"""
Test 1: 'tri'
expected output
    ger
    onometry
"""
print(f('tri'))

"""
Test 2:(edge case) no match
expected output
    Error: 'rat' not found
"""
print(f('rat'))

"""
Test 3:(edge case) empty string
expected output
    NaN
"""
print(f(''))



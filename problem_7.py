#!/usr/bin/env python
# coding: utf-8

# In[15]:


"""
Bharat Raman: Problem 7
Navigating Router via Trie
"""

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = ""):
        self.root = TrieNode("root handler")

    def insert(self, full_path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        currentNode = self.root #start at root
        for p in full_path: #
            if p not in currentNode.children:
                currentNode.children[p] = TrieNode()
            currentNode = currentNode.children[p]
        currentNode.handler = handler #assign handler to deepest node in this trie path
        
    def find(self, full_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        ## Find the Trie node that represents this prefix
        currentNode = self.root
        for p in full_path:
            if p in currentNode.children:
                currentNode = currentNode.children[p]
            else:
                return None
        return currentNode.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class TrieNode:
    def __init__(self, handler = "No handler found"):
        self.children = {}
        self.handler = handler

    def insert(self, char):
        self.children[char] = TrieNode()
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        self.routes = RouteTrie()
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        full_path = self.split_path(path)
        self.routes.insert(full_path, handler)


    def lookup(self, path):
        full_path = self.split_path(path)
        result = self.routes.find(full_path)
        if result == "":
            return None
        return result


    def split_path(self, path):
        path = path[1:]
        path_list = path.split('/')
        if path_list[-1] == '':
            path_list = path_list[:-1]
        return path_list
    
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
"""
Test 1: handler found
expected output:
    about handler
"""
print(router.lookup("/home/about/"))
"""
Test 2:(edge case) No directory present
expected output:
    None
"""
print(router.lookup("/home/applications/"))

"""
Test 3: (edge case) no handler found
expected output:
    No handler found
"""
print(router.lookup("/home/"))


# In[ ]:





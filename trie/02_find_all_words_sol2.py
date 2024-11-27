"""
Given a trie data structure representing a list of words, implement a function that finds and returns all words stored
in the trie.


This solution utilizes a trie data structure, efficiently organizing a list of words. In a trie, each word is broken
down into letters, each represented by a node in the trie. Starting from the root node, each subsequent letter in the
word corresponds to a child node of the previous letter’s node. This process continues until the entire word is
represented by a path from the root node to a node marked as the end of the word. The algorithm explores each node by
recursively traversing the trie from the root node, effectively enumerating all possible character combinations that
form valid words. At each node, it checks if it marks the end of a word, constructing the word by accumulating
characters from the word array. This recursive exploration continues until all words in the trie are found and stored
in the result list. Let’s look at how each function behaves and contributes to this approach:

    The get_max_depth function recursively determines the maximum depth of a tree. It starts from a given root node and
    traverses through the tree’s children, incrementing the level by one each time. This recursive traversal continues
    until it reaches the leaf nodes. At each level, the function compares the current depth with the maximum depth
    encountered so far, updating the maximum depth if necessary.

    The find_words function recursively retrieves words from a tree structure. It initializes an empty list to store
    words and a list with a size determined by the tree’s maximum depth. As it traverses the tree, it retrieves the
    characters at each level to form words, appending them to the result list when a word is complete. Finally, it
    returns the list of extracted words.

    The get_words function utilizes a depth-first search (DFS) approach to traverse a trie data structure. It starts
    from the given root node and recursively explores each branch. At each node, the algorithm checks if it marks the
    end of a word. If it does, it constructs the word by concatenating characters stored in the word array to the
    current level and adds it to the result list. Then, the algorithm iterates over the current node’s children,
    representing possible next characters in the words. For each child, it updates the word array with the character at
    the current level and recursively explores the child node. This process continues until all possible paths in the
    trie are explored, generating all words stored in the trie.

Time complexity

The time complexity of this solution is O(n), where n is the total number of characters in all words stored in the trie.
This complexity arises from traversing each trie node once to retrieve the words.

Space complexity

The space complexity of the provided code is O(n+m), where n is the total number of characters in all words stored in
the trie, and m is the length of the longest word.
##################################
This is the same as trie/03_list_sort.py
"""
from Trie import Trie
from TrieNode import TrieNode

from Trie import Trie
from TrieNode import TrieNode


# Recursive function to get the maximum depth of a trie
def get_max_depth(root, level):
    # If the root is null, return the current level
    if not root:
        return level
    max_depth = level
    for child in root.children:
        # Recursively calculate the maximum depth of the subtree
        max_depth = max(max_depth, get_max_depth(child, level + 1))
    return max_depth


# Recursive function to find all the words stored in a trie
def get_words(root, result, level, word):
    # If the current node marks the end of a word, construct the word and append it to the result list
    if root.is_end_word:
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(str(temp))

    for i in range(26):
        if root.children[i]:
            # Update the word array with the character at the current level
            word[level] = chr(i + ord("a"))

            # Recursively explore the child node
            get_words(root.children[i], result, level + 1, word)


# Helper function to call the get_words function
def find_words(root):
    result = []
    word = [None] * get_max_depth(root, 0)
    get_words(root, result, 0, word)
    return result


# Driver Code
def main():
    num = 1
    words = [
        ["gram", "groom", "ace", "act", "actor"],
        ["abs", "crow", "crop", "abstain", "crunch"],
        ["dorm", "norm", "prom", "loom", "room"],
        ["prey", "prep", "press", "preps", "prefix"],
        ["moon", "once", "face", "dice", "mole"],
    ]

    for word in words:
        t = Trie()
        for w in word:
            print("Insert word: '", w, "'", sep="")
            t.insert(w)
            num += 1
            words_found = find_words(t.root)
        print("\nWords found: ", words_found, sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

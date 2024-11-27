"""
Given a dictionary, find whether a given word can be formed by combining two words from the dictionary.

The solution leverages the trie data structure to efficiently search words in the dictionary.
A trie represents each word as a sequence of nodes, with each node corresponding to a letter in the word.
This enables quick access to words with common prefixes.

In this scenario, we have a dictionary of words.
The objective is to check if a given word can be constructed by combining two words from this dictionary.
Leveraging the trie data structure for this problem provides several advantages.
Trie efficiently organizes words based on their prefixes, enabling swift searches and comparisons,
essential for determining word formation.

In a naive approach, if the prefixes of the given word are searched directly in the dictionary (list of words),
the time complexity would grow to O(n × m^2), where:
  - n is the length of the dictionary
  - m is the length of the given word
The trie data structure optimizes the search operation by only visiting the words with the required prefix
instead of visiting all words in the dictionary.

Let’s walk through the steps of the solution:

1. Create a trie and populate it with the words from the dictionary.

2. Search for a complete prefix of the word in the trie.

3. If a complete prefix is found, search for the remaining string of the word in the trie.

4. If the remaining string of the word is also found in the trie, return TRUE, otherwise return FALSE.

This algorithm ensures a quick and accurate determination of word formation,
making it an effective approach for the problem at hand.

Time Complexity:
The time complexity of this solution is O(m + n), where:
  - m is the number of words in the dictionary
  - n is the length of the word
Insertion of all the words from the dictionary into the trie takes O(m) time,
and traversing each letter in the word takes O(n) time.

Space Complexity:
The space complexity is O(m), where:
  - m is the number of words in the dictionary
This is because we insert all the words from the dictionary into the trie.
"""
from Trie import Trie
from TrieNode import TrieNode


def is_formation_possible(dictionary, word):
    my_trie = Trie()
    for item in dictionary:
        my_trie.insert(item)

    current = my_trie.root
    word = word.lower()
    end_count = 0
    for letter in word:
        index = ord(letter) - ord("a")
        if current.children[index]:
            print(f"index = {index} char = {current.children[index].char}")
            if current.children[index].char != letter:
                return False
            elif current.children[index].is_end_word:
                end_count += 1
                current = my_trie.root
            else:
                current = current.children[index]

    print(end_count)
    if end_count == 2:
        return True

    return False


def main():
    inputs = [
        ["he", "hello", "home", "work"],
        ["play", "plot", "bat"],
        ["p", "q", "r"],
        ["abc", "def", "xyz"],
        ["add", "addi", "number"],
    ]

    words = ["hehome", "world", "pr", "abcdefxyz", "adaddi"]

    for i in range(len(inputs)):
        print("\tDictionary: ", inputs[i], sep="")
        print("\tword: ", words[i], sep="")
        print("\n\tResult: ", is_formation_possible(inputs[i], words[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

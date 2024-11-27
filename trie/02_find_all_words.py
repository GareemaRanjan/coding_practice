"""
Given a trie data structure representing a list of words, implement a function that finds and returns all words stored
in the trie.



"""
from Trie import Trie
from TrieNode import TrieNode


def find_words(root, prefix=""):
    """
    Recursively finds all the words stored in the trie.

    Args:
        root: The current trie node.
        prefix: The prefix formed so far.

    Returns:
        A list of words stored in the trie.
    """
    if not root:
        return []

    words = []

    # If the current node represents the end of a word, add it to the list
    if root.is_end_word:
        words.append(prefix)

    # Recur for all children
    for child in root.children:
        if child:  # If the child node exists
            words.extend(find_words(child, prefix + child.char))

    return words


def main():
    num = 1
    keys = [
        ["hello", "world", "python", "programming"],
        ["app", "apple", "applepie"],
        ["dog", "dig", "ham", "hamster", "dino"],
        ["sun", "burn"],
        ["red", "blue", "green", "yellow", "orange", "purple"],
    ]

    for words in keys:
        t = Trie()
        for word in words:
            t.insert(word)
            num += 1
        words_found = find_words(t.root)
        print("\nTotal words found: ", words_found, sep="")
        print("-" * 50)


if __name__ == "__main__":
    main()

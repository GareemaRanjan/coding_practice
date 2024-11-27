"""
Statement
Given a trie data structure that represents a list of words, words, determine the total number of words stored in it.

Solution
The solution leverages the given trie data structure to efficiently organize and process a list of words. A trie
represents each word as a sequence of nodes, with each node corresponding to a letter in the word. This ensures quick
access to words based on common prefixes. The algorithm starts at the root node and recursively explores all child nodes
while keeping the count of the total words. This effectively enumerates all possible word combinations.

Here are the steps of this solution:

    1.Initialize a counter, result, to 0.

    2.Traverse the complete trie. Start from the root node and process each node encountered as follows:

        i.If the node marks the end of a word, increment the result counter.

        ii.Recursively traverse all non-null children nodes of the current node.

    3.Return result.

Time complexity

The time complexity of this solution is O(n), where n is the total number of nodes in the trie. This complexity arises
from traversing each trie node exactly once to retrieve the word count.

Space complexity

The space complexity of the provided code is O(m), where is the total number of characters in all the words stored in
the trie.
"""
from Trie import Trie

# TrieNode => {children, is_end_word, char}


def total_words(root):
    count = 0  # Initial count for each node

    for child in root.children:  # Loop through each child node of the root
        if child:  # Check if the child node exists
            # print(child.char)  # Print the current character for debugging

            if child.is_end_word:  # If this node represents the end of a word
                count += 1  # Increment count because a word ends here
            #     print(f"END WORD {child.char}, count updated {count}")
            # else:
            #     print(f"Not end word {child.char}, count found {count}")

            # Recursive Call (Drilling Down):
            # - count += total_words(child) calls total_words on each child node.
            # - This goes one level deeper in the trie, now analyzing the children of `child`.
            # - Each recursive call starts with count = 0 for that subtree,
            #   then accumulates based on the `is_end_word` checks in its own children.
            count += total_words(
                child
            )  # Recursively call total_words on the child and add its result to count

    # Returning from Recursive Calls (Climbing Back Up):
    # - Each call to total_words(child) will finish once all descendants of `child` are processed.
    # - When a subtree finishes counting words, that count returns up to the parent level
    #   and gets added to the count there.
    # - Finally, when all children of the root have been processed,
    #   total_words(root) returns the total word count for the entire trie.
    return count  # Return the total word count found from this root node and its descendants


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
            words_found = total_words(t.root)
        print("\nTotal words found: ", words_found, sep="")
        print("-" * 50)


if __name__ == "__main__":
    main()

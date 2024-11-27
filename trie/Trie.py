from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t) - ord("a")

    def insert(self, key):
        """
        For a key with n characters, the worst case time complexity turns out to be O(n) since we need to make n
        iterations.
        """
        if key is None:
            return False
        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        key = key.lower()
        current = self.root
        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                # print(letter, "inserted")
            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                # print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print(
                    "- Node",
                    current.char,
                    ": has children, don't delete \
                it",
                )
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print(
                        "- - Don't delete node",
                        current.char,
                        ": has \
                    children",
                    )
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        print("\nDeleting:", key)
        self.delete_helper(key, self.root, len(key), 0)

    def search(self, key):
        """

        Time complexity:
        If the length of the word is h, the worst-case time complexity is O(h). In the worst case, we have to look at h
        consecutive levels of a trie for a character in the key being searched for. The presence or absence of each
        character from the key in the trie can be determined in O(1) because the size of the alphabet is fixed. Thus,
        the running time of search in a trie is O(h).

        :param key:
        :return:
        """
        key = key.lower()
        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key
        current = self.root
        for letter in key:
            index = self.get_index(letter)
            if (
                current.children[index] is None
                or current.children[index].char != letter
            ):
                # print(f"\tReturning false. current.children[index]={current.children[index]}, letter={letter}")
                return False

            current = current.children[index]

        if not current.is_end_word:
            return False

        return True


if __name__ == "__main__":
    keys = [
        "the",
        "a",
        "there",
        "answer",
        "any",
        "by",
        "bye",
        "their",
        "abc",
        "gareema",
    ]

    t = Trie()
    print("Keys to insert:\n", keys)

    # Construct Trie
    for words in keys:
        t.insert(words)

    print(f"Searching for gareema : {t.search('gareema')}")
    print(f"Searching for gareem : {t.search('gareem')}")
    print(f"Searching for gareemaranjan : {t.search('gareemaranjan')}")
    print(f"Searching for akshat : {t.search('akshat')}")
    print(f"Searching for greems : {t.search('greems')}")

    res = ["Not present in trie", "Present in trie"]

    t = Trie()
    print("Keys to insert: \n", keys)

    # Construct Trie
    for words in keys:
        t.insert(words)

    # Search for different keys
    print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
    print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
    print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])

    # Delete abc
    t.delete("abc")
    print('Deleted key "abc" \n')

    print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])

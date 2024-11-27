class TrieNode:
    def __init__(self, char=""):
        self.children = [None] * 26
        self.char = char
        self.is_end_word = False

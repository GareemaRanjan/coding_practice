"""
Given a list of words words_list, determine whether a given target can be formed by combining two words from the list
in any order.

Solution:

In this solution, we aim to determine the possibility of forming a target word by combining two words from a list.
Initially, we check all possible divisions of the target word into two parts. First, we insert all the words in the list
into the hash table. Then, we iterate over each position in the target word, creating a prefix and a suffix. For each
division, we check if the prefix and suffix exist in the hash table. If both are found in the hash table, we return
TRUE, confirming that the target word can be formed. If no such combination is found in the hash table after checking
all possible divisions, we return FALSE, indicating that the target word cannot be formed using two words from the
given list.

Let’s look at the steps of the algorithm:

    - Create a hash table of all the words in the words_list.

    - Start by iterating over the characters of the target to check all possible divisions.

    - For each index, divide the word into two parts: a prefix and a suffix.

        - The prefix consists of the characters from index 0 to i-1

        - The suffix consists of the characters from index i to the end of the word.

    - Check if the prefix and suffix exist in the hash table. This is done to see if each part of the divided word is
    present in the hash table or not.

        - If the prefix and suffix are found in the hash table, return TRUE, indicating that the word can be formed by
        combining two words from the table.

        - Otherwise, keep iterating to check other possible divisions.

    - If no such combination is found after iterating over the target to check all possible divisions, return FALSE,
    indicating that the word cannot be formed using two words from the hash table.

Time complexity

The time complexity of this solution is O(n+m), where n is the number of elements in words_list, and m is the length of
the target. This is because insertion in the hash table requires n time, and iterating over the target requires m time.

Space complexity

The space complexity of this solution is O(n), where n is the number of elements in words_list. This is because the
hash table takes n space to store the words.
"""
def is_formation_possible(words_list, target):
    my_list = set(words_list)
    for i in range(1, len(target)):
        print(f"{target[0:i]} {target[i:len(target)]}")
        sub1 = target[0:i]
        sub2 = target[i:len(target)]
        if sub1 in my_list and sub2 in my_list:
            return True

    return False


def main():
    words_list = [["flower", "moon", "plant", "sun", "star"],
                  ["sand", "water", "fly"],
                  ["paper", "pen", "book", "page", "note", "pencil"],
                  ["door", "light", "window", "balcony", "attic", "roof"],
                  ["bow", "rain"]]
    targets = ["sunflower", "waterfall", "notebook", "lighthouse", "rainbow"]

    for i in range(len(words_list)):
        print("Words in the table:", words_list[i])
        print("Target word:", targets[i])
        print("Found:", is_formation_possible(words_list[i], targets[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
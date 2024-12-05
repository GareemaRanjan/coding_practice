def linear_search(lst, key):
    """
    Linear search function
    :param lst: lst of unsorted integers
    :param key: A key to be searched in the list
    """
    if len(lst) <= 0:  # Sanity check
        return -1

    for i in range(len(lst)):
        if lst[i] == key:
            return i  # If found return index
    return -1  # Return -1 otherwise


# Driver code to test above
if __name__ == "__main__":

    lst = [5, 4, 1, 0, 5, 95, 4, -100, 200, 0]
    key = 95

    index = linear_search(lst, key)
    if index != -1:
        print("Key:", key, "is found at index:", index)
    else:
        print(key, " is not found in the list.")

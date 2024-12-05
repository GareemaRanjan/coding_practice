def binary_search(lst, key):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if key == lst[mid]:
            return mid
        elif key > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":

    lst = [1, 2, 3, 10, 20, 40, 111, 244, 14444, 800000]
    key = 111

    # Function call
    result = binary_search(lst, key)

    if result != -1:
        print("Element is present at index:", result)
    else:
        print("Element is not present in the list")

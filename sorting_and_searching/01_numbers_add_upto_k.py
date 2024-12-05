"""
In this problem, you have to implement the find_sum(lst, n) function which will take a list lst and number n as inputs
and return two numbers from the list that add up to n.

Input
A list and a number n

Output
A list with two integers a and b that add up to n

Solution
For each element in the list, use a binary search to look for the difference between that element and the intended sum.
You can implement the binary_search function however you like, recursively or iteratively. So, if the intended sum is n
and the first element of the sorted list is a0, then you will conduct a binary search for n-a0 and so on for every a,
i.e., an until one is found.

Time complexity
Since most popular sorting functions take O(nlogn), let’s assume the built-in function in Python,.sort() function
takes the same. Then, a binary search for each element takes O(logn), so a binary search for all n elements will take
O(nlogn). So, the overall time complexity is O(nlogn).


"""


def binary_search(lst, key):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # print(f"mid = {mid}")
        if lst[mid] == key:
            # print("found")
            return True
        elif lst[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
        # print(f"left = {left}, right = {right}")

    return False


def find_sum(lst, n):
    lst.sort()
    for num in lst:
        comp = n - num
        if binary_search(lst, comp):
            return [num, comp]

    return []


print(find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))

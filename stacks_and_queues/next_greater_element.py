"""
Problem Statement
You are required to implement the next_greater_element() function. For each element i
in a list, the function finds the first element to its right which is greater than element i.
If for any element such a value does not exist, the answer is -1.

Note: The next greater element is the first element towards the right which is greater than the given element.
For example, in the list [1, 3, 8, 4, 10, 5], the next greater element of 3 is 8 and the next greater element for
8 is 10.


Input
An integer list.

Output
A list containing the next greater element of each element from the input list.

Sample Input
list = [4, 6, 3, 2, 8, 1]
Sample Output
result = [6, 8, 8, 8, -1, -1]


------------------------------------------------------------------------------------------------------------------------

Solution: In this solution, we use our own MyStack and res, a Python list.

The outer for loop begins from the end of lst. In each iteration, the top of the stack is compared with the current
element in lst. Whenever the current value in lst is larger than top, that value is the next greater element in the
list.

The top is popped and the current element in the list is again compared with the new top of the stack in the inner
while loop. This loop stops when the top of the stack is bigger than the element of the list or the stack becomes
empty.

If the stack is empty, it implies that the current element in lst does not have a next greater element. Hence, its
corresponding index in res would retain the value of -1.

If the stack is not empty, then the current element has a value larger than it. Hence, the top value will be
assigned to the corresponding index in res.

Continuing this process, we end up with a list containing all the next greater elements for all indices of lst.
------------------------------------------------------------------------------------------------------------------------

####
At any instance, if we find that current elemt is greater than peek, we pop the list till we reach a number greater
than the current number.
------------------------------------------------------------------------------------------------------------------------

Time complexity:

O(n^2) for worst case.
"""

from Stack import MyStack


def find_next(l):
    res = [-1] * len(l)
    mystack = MyStack()
    for i in range(len(l) - 1, -1, -1):

        if mystack.is_empty():
            res[i] = -1

        elif mystack.peek() > l[i]:
            res[i] = mystack.peek()

        else:
            while not mystack.is_empty() and mystack.peek() < l[i]:
                mystack.pop()
            if mystack.is_empty():
                res[i] = -1
            else:
                res[i] = mystack.peek()
        mystack.push(l[i])

        print(f"stack = {mystack.stack_list}")
    print(res)
    return res


if __name__ == "__main__":
    assert find_next([7, 10, 1, 2, 3, 4, 5, 6]) == [10, -1, 2, 3, 4, 5, 6, -1]

    assert find_next([4, 6, 3, 2, 8, 1]) == [6, 8, 8, 8, -1, -1]
    find_next([1000] + list(range(1, 100)))

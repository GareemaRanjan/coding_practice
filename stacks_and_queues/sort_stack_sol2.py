"""
Problem Statement
Implement a function called sort_stack() which takes a stack and sorts all of its elements in ascending order such that when they are popped and printed, they come out in ascending order. So the element that was pushed last to the stack has to be the smallest.

Input
A stack of integers.

Output
The stack with all its elements sorted in descending order.

Sample Input#
stack = [23, 60, 12, 42, 4, 97, 2]
Sample Output
result = [97, 60, 42, 23, 12, 4, 2]

------------------------------------------------------------------------------------------------------------------------

Solution: Recursive Sort

The idea is to pop out all the elements from the stack in one recursive call. Once the stack is empty,
we will push back values in a sorted order using the insert function.

At each call, we receive a partially sorted stack in which we insert the value being popped out at that recursive call.
 If the value is smaller than the top element if the stack, we simply push it to the top.

Otherwise, we call insert again until we can find the appropriate place for the value in the stack.
------------------------------------------------------------------------------------------------------------------------

#### Inner loop is to move each element to its right position. Temp stack will have elements already in order.
------------------------------------------------------------------------------------------------------------------------

Time complexity:

The sortStack function is recursively called on all n elements. In the worst case, there are n calls to insert for
each element. This pushes the time complexity up to O(n2).
"""

from Stack import MyStack


def sort_stack(stack):
    if not stack.is_empty():
        value = stack.pop()
        sort_stack(stack)
        insert(stack, value)


def insert(stack, value):
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)


if __name__ == "__main__":
    mystack = MyStack()
    mystack.push(97)
    mystack.push(2)
    mystack.push(4)
    mystack.push(42)
    sort_stack(mystack)
    print(mystack.print())

"""
Problem Statement
You have to implement the MinStack class which will have a min() function. Whenever min() is called,
the minimum value of the stack is returned in O(1) time. The element is not popped from the stack. Its
value is simply returned.

Input
min() operates on an object of MinStack and doesn’t take any input

Output
Returns minimum number in O(1) time

Sample Input
Main stack: [5, 0, 2, 4, 1, 3, 0]
Sample Output
Minimum value: 0


------------------------------------------------------------------------------------------------------------------------

Solution: The whole implementation relies on the existence of two stacks, min_stack and main_stack.

main_stack holds the actual stack with all the elements, whereas min_stack is a stack whose top always contains
the current minimum value in the stack.

How does it do this? The answer is in the push() function. Whenever push() is called, main_stack simply inserts
it at the top. However, min_stack checks the value being pushed. If min_stack is empty, this value is pushed into
it and becomes the current minimum. If min_stack already has elements in it, the value is compared with the stack’s
top element. The element is inserted if it is smaller than the top element; otherwise, we insert the top element again.

The pop() function pops off from the main_stack and min_stack as usual.

Due to all these safeguards we’ve put in place, the min() function only needs to return the value at the top of
min_stack.
------------------------------------------------------------------------------------------------------------------------

####
------------------------------------------------------------------------------------------------------------------------

Time complexity:

Our goal was to create a stack that returns the minimum value in constant time. As we can see in the algorithm above,
the min() function truly works in O(1).
"""

from Stack import MyStack
import pandas as pd

class MinStack:
    def __init__(self):
        self.stack = MyStack()
        self.min_stack = MyStack()

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def push(self, value):
        self.stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())

    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        return None


if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    print("Main stack:", stack.stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))

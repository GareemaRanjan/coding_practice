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

Solution: Using a Temporary Stack

1. Use a second temp_stack.
2. Pop value from mainStack.
3. If the value is greater or equal to the top of temp_stack,
  then push the value in temp_stack
  else pop all values from temp_stack
      and push them in mainStack
      and in the end push value in temp_stack
4.repeat from step 2 till mainStack is not empty.
5. When mainStack will be empty,
    temp_stack will have sorted values in descending order.
6. Now transfer values from temp_stack to mainStack
    to make values sorted in ascending order.

This solution takes an iterative approach towards the problem. We create a helper stack called temp_stack.
Its job is to hold the elements of stack in descending order.

The main functionality of the algorithm lies in the nested while loops. In the outer loop, we pop elements out of
stack until it is empty. As long as the popped value is larger than the top value in temp_stack, we can push it in.

The inner loop begins when stack.pop() gives us a value which is smaller than the top of temp_stack. All the elements
(they are sorted) of temp_stack are shifted back to stack and the value is pushed into temp_stack. This ensures that
the bottom of temp_stack always holds the smallest value from stack.

When stack becomes empty, all the elements are in temp_stack in descending order. Now we simply push them back into
stack, resulting in the whole stack being sorted in ascending fashion.
------------------------------------------------------------------------------------------------------------------------

#### Inner loop is to move each element to its right position. Temp stack will have elements already in order.
------------------------------------------------------------------------------------------------------------------------

Time complexity:

The outer and inner loops both traverse all the n elements of the stack. Hence, the time complexity is O(n2).
"""

from Stack import MyStack


def sort_stack(stack):
    temp_stack = MyStack()
    while not stack.is_empty():
        value = stack.pop()
        if temp_stack.is_empty() or value <= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and value > temp_stack.peek():
                stack.push(temp_stack.pop())
            temp_stack.push(value)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return stack


if __name__ == "__main__":
    mystack = MyStack()
    mystack.push(97)
    mystack.push(2)
    mystack.push(4)
    mystack.push(42)
    print(sort_stack(mystack).print())

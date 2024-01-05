"""
Problem Statement
You have to implement the enqueue() and dequeue() functions using the MyStack class we created earlier.
enqueue( ) will insert a value into the queue and dequeue( ) will remove a value from the queue.

Input
enqueue( ): A value to insert into the queue
dequeue( ): Does not require any input

Output
enqueue( ): Does not return anything
dequeue( ): Pops out and returns the oldest value in the queue

------------------------------------------------------------------------------------------------------------------------

Solution: Two Stacks Working in dequeue()

In this approach, we make dequeue the more expensive operation. enqueue works in constant time as we simply push
the value into main_stack.

In dequeue, we first check if temp_stack is empty. If it is, then we move all the elements of main_stack to temp_stack
 (given that main_stack is not empty). This would bring the oldest element to the top of temp_stack. Now, all we have
 to do is pop off the top value.

However, if temp_stack was not empty at the beginning, then we would not transfer any elements. The top value in
temp_stack would simply be popped off and returned.
------------------------------------------------------------------------------------------------------------------------

### Inverse main stack contents into new stack at the time of dequeue.
### Enqueue always happens in main stack. Dequeue always happens in new_stack.
------------------------------------------------------------------------------------------------------------------------

Time complexity:

enqueue()
In the second approach, enqueue operation takes constant time.

dequeue()
dequeue is O(n) if temp_stack is empty because in that case, we have to transfer all the elements to it. However,
it takes O(1) as temp_stack is not empty. This solution is more efficient than the previous one because, each time,
we perform one transfer instead of two, and sometimes we do not need to transfer at all.
"""

from Stack import MyStack


class newQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.new_stack = MyStack()

    def enqueue(self, value):
        self.main_stack.push(value)

    def dequeue(self):
        while not self.main_stack.is_empty():
            self.new_stack.push(self.main_stack.pop())
        return self.new_stack.pop()

    def print(self):
        print("**********")
        print(f"Main stack = {self.main_stack.stack_list}")
        print(f"New stack = {self.new_stack.stack_list}")


if __name__ == "__main__":
    myqueue = newQueue()
    print(myqueue.dequeue())
    myqueue.enqueue(1)

    myqueue.enqueue(2)
    myqueue.enqueue(3)
    print(myqueue.dequeue())
    myqueue.enqueue(4)

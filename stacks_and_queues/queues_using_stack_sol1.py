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

Solution: Two Stacks Working in enqueue()

In this approach, we are using two stacks. The main_stack stores the queue elements while the temp_stack acts as a
temporary buffer to provide queue functionality.

We make sure that after every enqueue operation, the newly inserted value is at the bottom of the main stack.
Before insertion, all the other elements are transferred to temp_stack and, naturally, their order is reversed.
The new element is added into the empty main_stack. Finally, all the elements are pushed back into main_stack
and temp_stack becomes empty.

The dequeue operation simply pops out the element at the top of main_stack that is the oldest element in the stack.

We can observe that the meat of the implementation lies in enqueue making it a costly operation.
------------------------------------------------------------------------------------------------------------------------

#### Every enqueue will reverse the stack
#### Pop will always happen from main stack
------------------------------------------------------------------------------------------------------------------------

Time complexity:

enqueue()
Whenever a value is enqueued, all the elements are transferred to temp_stack and then back to main_stack. Hence, for n elements in our queue, the runtime complexity of the enqueue operation is O(n).

dequeue()
The dequeue operation takes constant time since it involves one pop of the stack.

"""

from Stack import MyStack


class newQueue:
    def __init__(self):
        self.main_stack = MyStack()
        self.new_stack = MyStack()

    def enqueue(self, value):
        if self.main_stack.is_empty():
            self.main_stack.push(value)
        else:
            # every enqueue will reverse the stack
            while not self.main_stack.is_empty():
                self.new_stack.push(self.main_stack.pop())
            self.main_stack.push(value)
            while not self.new_stack.is_empty():
                self.main_stack.push(self.new_stack.pop())

    def dequeue(self):
        if self.main_stack.is_empty():
            return None
        return self.main_stack.pop()

    def print(self):
        print("**********")
        print(f"Main stack = {self.main_stack.stack_list}")
        print(f"New stack = {self.new_stack.stack_list}")


if __name__ == "__main__":
    myqueue = newQueue()
    print(myqueue.dequeue())
    myqueue.enqueue(1)

    myqueue.enqueue(2)
    myqueue.print()
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    myqueue.enqueue(5)
    myqueue.print()
    for i in range(0, 6):
        print(myqueue.dequeue())

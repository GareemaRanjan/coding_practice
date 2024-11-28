# Tutorial on Python's Default Heap Implementation (heapq)

# Python has a built-in library called 'heapq' which provides functions to implement a heap queue (priority queue).
# By default, 'heapq' provides a Min-Heap implementation.
# In this tutorial, we will explore the basics of 'heapq' usage with clear examples and explanations.

import heapq

# Creating a Min-Heap
# In Python, heapq by default creates a Min-Heap. Let's create one and understand the usage:

# Initialize an empty list to be used as a heap
min_heap = []

# Adding elements to the heap
# The 'heapq.heappush(heap, elem)' function is used to push elements into the heap while maintaining the heap property.
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 10)

# Printing the heap
# The internal structure of the heap is represented as a list, and it will maintain the properties of a Min-Heap.
print("Min-Heap after inserting elements:", min_heap)

# Removing the smallest element from the heap
# The 'heapq.heappop(heap)' function removes and returns the smallest element from the heap.
smallest = heapq.heappop(min_heap)
print("Removed the smallest element:", smallest)
print("Min-Heap after removing the smallest element:", min_heap)

# Converting a list into a heap
# We can also convert an existing list into a heap using 'heapq.heapify(list)'
existing_list = [50, 20, 30, 10, 40, 15]
heapq.heapify(existing_list)
print("Heapified list:", existing_list)

# Using a heap as a priority queue
# The heapq module can be used as a priority queue where the smallest priority value is accessed first.
heapq.heappush(existing_list, 5)
print("Heap after adding element with priority 5:", existing_list)

# Implementing a Max-Heap using heapq
# Since 'heapq' provides only a Min-Heap by default, we can simulate a Max-Heap by inserting negative values.
max_heap = []
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -10)

# To get the largest element, we need to pop and negate the value
largest = -heapq.heappop(max_heap)
print("Removed the largest element from Max-Heap:", largest)
print(
    "Max-Heap after removing the largest element:", [-elem for elem in max_heap]
)  # Printing with positive values for clarity

# Summary of heapq usage:
# 1. heapq.heappush(heap, elem) - Adds an element while maintaining heap properties.
# 2. heapq.heappop(heap) - Removes and returns the smallest element from the heap.
# 3. heapq.heapify(list) - Converts a list into a heap in-place.
# 4. Max-Heaps can be simulated by pushing negative values.

# In real-world applications, 'heapq' can be used for implementing efficient priority queues,
# scheduling algorithms, or any scenario that requires quick access to the smallest or largest element.

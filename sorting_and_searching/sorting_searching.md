# Sorting

**Sorting** is the process of arranging items systematically. In computer science, sorting algorithms arrange elements of a list in a specific order. The most commonly used orders are:

- **Numerical Order**: Sorting according to numbers.
- **Lexicographical Order**: Sorting according to letters (like alphabetical order).

Efficient sorting is crucial for optimizing the performance of other algorithms that require sorted input or need sorting as part of their process.

## Sorting Algorithms

Let’s discuss a few common sorting algorithms.

### Selection Sort Algorithm

**Selection Sort** is a simple sorting algorithm that works by repeatedly finding the minimum element in the unsorted list and placing it at the beginning. It maintains two sublists:

1. **Sorted Sublist**: This sublist is built from left to right and contains the already sorted elements.
2. **Unsorted Sublist**: This sublist contains the elements that still need to be sorted.

The algorithm works by iterating over the unsorted list and swapping each element with the minimum (or maximum) element found in the unsorted sublist, moving it to the sorted sublist.

### Time Complexity of Selection Sort

The time complexity of **Selection Sort** is **O(n²)**, where `n` is the number of elements in the list. This is because:

- Finding the minimum element in the unsorted list requires iterating over the entire list.
- The process is repeated for each element in the list, resulting in a quadratic time complexity.

This makes **Selection Sort** impractical for large datasets due to its inefficiency in handling large inputs.

# Insertion Sort

**Insertion Sort** is a simple and intuitive sorting algorithm that works similarly to how you might sort playing cards in your hands. It iterates over the given list, determines the correct position of each element, and inserts it into its correct position.

### How Insertion Sort Works

1. Start with the second element of the list.
2. Compare the current element to the one before it. If the current element is smaller, move the previous element one position to the right.
3. Repeat this process for each element, moving them into the correct position one at a time.

By the end, the algorithm produces a sorted list.

### Time Complexity of Insertion Sort

- **Worst Case**: **O(n²)**, which occurs when the list is sorted in reverse order.
- **Best Case**: **Ω(n)**, which occurs when the list is already sorted. In this case, the algorithm only needs to do a single pass over the list, making it much faster.

### Space Complexity of Insertion Sort

- **Space Complexity**: **O(1)**, since Insertion Sort is an **in-place** sorting algorithm. This means it doesn't require extra space for auxiliary data structures.

# Sorting Algorithms

## Merge Sort

**Merge Sort** is a recursive **divide and conquer** algorithm. The basic idea is to divide the list into two halves, recursively sort those halves, and merge them back together in order. The base case is when a sublist has only one element, at which point it is already sorted. The merging step is where most of the heavy lifting happens.

### Steps for Merge Sort:
1. **Divide**: Split the list into two halves.
2. **Recursively sort** each half.
3. **Merge** the two sorted halves into a single sorted list.

### Time Complexity of Merge Sort:
- **Best, Average, and Worst Case**: **O(n log n)**

---

## Quick Sort

**Quick Sort** is a comparison-based sorting algorithm and is considered the fastest known sorting algorithm for lists in the average case.

### Steps for Quick Sort:
1. **Start with a list of n elements**.
2. **Choose a pivot element** from the list to be sorted.
3. **Partition** the list into two sublists:
   - One sublist contains elements smaller than the pivot.
   - The other sublist contains elements greater than the pivot.
   - Elements equal to the pivot can go in either sublist.
4. **Recursively sort** each sublist.
5. **Concatenate** the two sorted sublists and the pivot to form one sorted list.

### How to Pick the Pivot:
There are several methods to choose the pivot:

1. **Choose Randomly**: Pick a pivot randomly from the list.
   - In this case, the probability of picking the same element at every recursive call decreases, leading to an asymptotic complexity of **O(n log n)** in the average case.

2. **Median of Three**: Pick three random elements from the list and choose the median. This strategy avoids picking the first element too often and leads to better performance in some cases.

### Time Complexity of Quick Sort:
- **Worst Case**: **O(n²)**, which occurs in the following cases:
  - The list is already sorted.
  - The list is sorted in reverse order.
  - All elements are identical.
  
- **Average Case**: **O(n log n)**, because the list is partitioned into sublists with roughly equal sizes at each recursive step.

---

## Quick Sort vs. Merge Sort

| Aspect              | Merge Sort                                  | Quick Sort                                |
|---------------------|---------------------------------------------|-------------------------------------------|
| **Merging**         | All the work is done during merging        | Simple concatenation of sublists         |
| **Dividing**        | Simple dividing of the list                | All the work is done during partitioning |
| **Time Complexity** | O(n log n) (best, average, worst case)     | O(n log n) (average), O(n²) (worst case) |
| **Space Complexity**| O(n) (due to auxiliary space for merging)  | O(log n) (due to recursion stack)        |
| **Stability**       | Stable sorting algorithm                   | Not stable                              |
| **Use Case**        | Better for linked lists                    | Generally faster on arrays              |

---

### Summary

- **Merge Sort** is efficient for large datasets and linked lists, with a stable O(n log n) time complexity.
- **Quick Sort** is generally faster for arrays but can degrade to O(n²) in the worst case, especially if the pivot is poorly chosen. Picking the pivot randomly or using the median of three improves performance.

# Sorting Algorithms Complexity Comparison

Below is a quick reference table for the **time complexity** of some well-known sorting algorithms in different cases: best, average, and worst.

| Algorithm       | **Best Case**         | **Average Case**      | **Worst Case**       |
|-----------------|-----------------------|-----------------------|----------------------|
| **Insertion Sort** | Ω(n)               | θ(n²)                 | O(n²)                |
| **Selection Sort** | Ω(n²)              | θ(n²)                 | O(n²)                |
| **Merge Sort**    | Ω(n log n)          | θ(n log n)            | O(n log n)           |
| **Quick Sort**    | Ω(n log n)          | θ(n log n)            | O(n²)                |
| **Bubble Sort**   | Ω(n)                | θ(n²)                 | O(n²)                |

### Key:
- **Best Case**: The best time complexity the algorithm can achieve.
- **Average Case**: The expected time complexity for a random input.
- **Worst Case**: The time complexity in the worst scenario (e.g., already sorted or reversed lists).

### Notes:
- **Insertion Sort**: Works well when the input is already partially sorted, with a best case of **Ω(n)**, but its worst case is **O(n²)**.
- **Selection Sort**: Always runs in **O(n²)**, making it inefficient for large lists.
- **Merge Sort**: Consistently performs in **O(n log n)** for best, average, and worst cases, and is a stable sort.
- **Quick Sort**: Has an average case of **O(n log n)** but can degrade to **O(n²)** if the pivot selection is poor (e.g., when the list is already sorted).
- **Bubble Sort**: Simple to implement, but inefficient with a worst-case time complexity of **O(n²)**. However, its best case is **Ω(n)** when the list is already sorted.

This table can be used as a quick reference to determine which sorting algorithm may be appropriate based on the nature of your input data and the performance needs.

# Searching Algorithms

## Brute Force: Linear Search

**Linear Search** is the simplest searching algorithm, where you go through each element in the list one by one. When the element you are searching for is found, its index is returned.

### How Linear Search Works:
1. Start from the first element of the list.
2. Compare each element with the target element.
3. If the element matches the target, return its index.
4. If the target element is not found, return `-1` to indicate that the element is not in the list.

### Performance of Linear Search:
- **Time Complexity**: **O(n)** in the worst case.
  - In the worst case, you will need to go through all `n` elements, where `n` is the length of the list.

---

## Binary Search

**Binary Search** is one of the most efficient searching algorithms and is typically used for searching in a sorted array. It divides the array into two halves and progressively reduces the search space, making it much faster than linear search for large datasets.

### How Binary Search Works:
1. **Assumption**: The input array must be sorted.
2. Compare the target element with the middle element of the array.
3. If the target matches the middle element, return the index of the middle element.
4. If the target element is greater than the middle element, recursively search the right half of the array.
5. If the target element is smaller than the middle element, recursively search the left half of the array.
6. Repeat the process, halving the search space until the element is found or the search space is empty.

### Implementation:
1. Set two pointers: `left` (initially 0) and `right` (initially the last index of the array).
2. Calculate the middle index: `mid = (left + right) / 2`.
3. Compare the target with `arr[mid]`:
   - If equal, return `mid`.
   - If the target is smaller, set `right = mid - 1` (search the left half).
   - If the target is larger, set `left = mid + 1` (search the right half).
4. Continue until the target is found or the `left` pointer exceeds the `right` pointer.

### Performance of Binary Search:
- **Time Complexity**: **O(log n)**.
  - Binary Search reduces the search space by half in each iteration, making it significantly faster than linear search for large arrays.

---

### Comparison

| **Algorithm**   | **Time Complexity (Best Case)** | **Time Complexity (Worst Case)** |
|-----------------|--------------------------------|---------------------------------|
| **Linear Search** | O(1)                           | O(n)                            |
| **Binary Search** | O(1)                           | O(log n)                        |

---

### Summary:
- **Linear Search** is simple and works on unsorted arrays but has a linear time complexity of **O(n)** in the worst case.
- **Binary Search** is much more efficient on sorted arrays with a time complexity of **O(log n)**, but it requires the list to be sorted beforehand.


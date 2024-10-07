"""
Question:
Given a compiled set of n tasks, represented by an array, task, and a neural network system with m nodes, each processes
tasks efficiently. For optimal performance, tasks must be distributed evenly across these nodes, i.e., all nodes should
serve the same number of tasks. Each task assigned to a single node must be different.

Maximize the number of tasks completed by allocating tasks effectively within the neural network and return the maximum
number of tasks completed using the distributed neural network system.

Note: All nodes must be assigned an equal number of tasks.

Input:
- n: an integer representing the number of tasks.
- task: an array of length n, representing the type of each task.
- m: an integer representing the number of nodes in the neural network system.

Output:
Return an integer representing the maximum number of tasks that can be completed by distributing tasks optimally.

Example:
n = 7
task = [1, 2, 2, 1, 3, 1, 3]
m = 2

One optimal way to allocate the tasks is:
- The 1st node works on the 1st, 2nd, and 5th tasks.
- The 2nd node works on the 3rd, 4th, and 7th tasks.

A total of 6 tasks can be accomplished this way.

Function Description:
Complete the function findMaximumTasks in the editor below.

findMaximumTasks takes the following parameter(s):
- int task[n]: the type of each task
- int m: the number of nodes in the neural network system

Returns:
- int: the maximum number of tasks that can be completed by distributing tasks optimally.

Constraints:
- 1 <= n <= 3 * 10^5
- 1 <= task[i] <= 10^9
- 1 <= m <= 10^9
"""


def findMaximumTasks(task, m):
    # Create a dictionary to count the frequency of each task type
    task_count = {}
    for t in task:
        if t in task_count:
            task_count[t] += 1
        else:
            task_count[t] = 1

    # Start calculating the maximum number of tasks that can be assigned fairly
    total_tasks = 0
    pending_tasks = {}
    for t in list(task_count.keys()):
        if task_count[t] >= m:
            total_tasks += 1

        else:
            pending_tasks[t] = task_count[t]

    sum_of_pending = 0
    for key, val in pending_tasks.items():
        sum_of_pending += val

    return (total_tasks + (sum_of_pending // m)) * m


# Example usage
n = 7
task = [1, 2, 2, 1, 3, 1, 3]
m = 2
print(findMaximumTasks(task, m))  # Output should be 6

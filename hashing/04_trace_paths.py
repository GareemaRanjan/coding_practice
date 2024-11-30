"""
Given a list 'paths', where each element 'paths_i' contains a pair of strings [source_i, destination_i]
representing a direct path from source_i to destination_i, the task is to return the correct sequence
of the entire journey from the first city to the last.

### Example:

Input:
paths = [["New York", "Chicago"], ["Boston", "Texas"], ["Missouri", "New York"], ["Texas", "Missouri"]]

Output:
[["Boston", "Texas"], ["Texas", "Missouri"], ["Missouri", "New York"], ["New York", "Chicago"]]

### Explanation:
- We are given a list of direct paths between cities.
- The goal is to reconstruct the full journey starting from the city that has no incoming path
  (i.e., the "start" city), and continuing to the city that has no outgoing path (i.e., the "end" city).

- Steps:
  1. Extract all the source cities and destination cities.
  2. Identify the "start" city as the one that is a source but not a destination.
  3. Identify the "end" city as the one that is a destination but not a source.
  4. Use a dictionary to quickly look up the next destination for each city.
  5. Reconstruct the journey by starting from the "start" city and following the paths until reaching the "end" city.

### Another Example:

Input:
paths = [["Sydney", "Dubai"], ["LosAngeles", "Cairo"], ["Paris", "Rome"], ["Cairo", "Paris"], ["Rome", "Tokyo"], ["Tokyo", "Sydney"]]

Output:
[["Sydney", "Dubai"], ["Dubai", "Cairo"], ["Cairo", "Paris"], ["Paris", "Rome"], ["Rome", "Tokyo"], ["Tokyo", "Sydney"]]


Time Complexity:
    Extracting the sources and destinations (Step 1): O(n)
    Finding the start and end cities (Step 2 and Step 3): O(n)
    Populating the dictionary (Step 4): O(n)
    Reconstructing the journey (Step 5): O(n)
Overall Time Complexity: O(n), where n is the number of paths
"""


def trace_path(paths):
    # Step 1: Find all sources and destinations
    source = set([i[0] for i in paths])  # Extract all source cities
    dest = set([i[1] for i in paths])  # Extract all destination cities

    # Step 2: Identify the start city
    start = list(source - dest)[0]  # Start city is in 'source' but not in 'dest'

    # Step 3: Identify the end city
    end = list(dest - source)[0]  # End city is in 'dest' but not in 'source'

    # Step 4: Build a dictionary for quick lookups
    my_dict = dict()  # Create an empty dictionary to map each source to its destination
    res = []  # Initialize the result list that will store the correct journey path

    # Fill the dictionary with the paths
    for item in paths:
        my_dict[item[0]] = item[1]  # Map each source to its corresponding destination
    print(my_dict)  # Optional: Print the dictionary for debugging

    # Step 5: Reconstruct the journey by following the paths
    while start and start != end:  # Continue until we reach the end city
        res.append([start, my_dict.get(start)])  # Add the current pair to the result list
        start = my_dict.get(start)  # Move to the next city by following the path

    return res  # Return the reconstructed path


# Example inputs
paths = [
    [["New York", "Chicago"], ["Boston", "Texas"], ["Missouri", "New York"], ["Texas", "Missouri"]],
    [["Sydney", "Dubai"], ["LosAngeles", "Cairo"], ["Paris", "Rome"], ["Cairo", "Paris"], ["Rome", "Tokyo"],
     ["Tokyo", "Sydney"]],
    [["Vienna", "Athens"], ["London", "Berlin"], ["Madrid", "Rome"], ["Paris", "Vienna"], ["Rome", "Paris"],
     ["Athens", "Moscow"], ["Berlin", "Madrid"]],
    [["Singapore", "Sydney"]],
    [["HongKong", "Taipei"], ["Osaka", "Seoul"], ["Taipei", "Singapore"], ["Tokyo", "Osaka"], ["Beijing", "Shanghai"],
     ["Seoul", "Beijing"], ["Singapore", "KualaLumpur"], ["Shanghai", "HongKong"]]
]

# Test cases
for i, path in enumerate(paths):
    print("{}. \tInput: {}".format(i + 1, path))
    print("\tOutput: {}".format(trace_path(path)))
    print("-" * 100)

"""
Implement a function that rearranges elements in a list so that all negative elements appear to the left and all
positive elements (including zero) appear to the right. It’s important to note that maintaining the original sorted
order of the input list is not required for this task.
"""


def rearrange(lst):
    res = [0] * len(lst)
    index = 0
    for i in range(0, len(lst)):
        if lst[i] < 0:
            res[index] = lst[i]
            index = index + 1

    for i in range(0, len(lst)):
        if lst[i] > 0:
            res[index] = lst[i]
            index = index + 1

    return res


def rearrange_inplace(lst):
    leftMostPosEle = 0
    for curr in range(len(lst)):
        # If negative number
        if lst[curr] < 0:
            # If not the last negative number
            if curr != leftMostPosEle:
                # Swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # Update the last position
            leftMostPosEle += 1
    return lst


def main():
    inputs = [
        [10, 4, 6, 23, 7],
        [-3, 20, -1, 8],
        [2, -5, -4, 43, 2],
        [-3, -10, -19, 21, -17],
        [25, 50, 75, 100, 400],
        [25, 50, 75, -1, -2],
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\n\tResult: ", rearrange(inputs[i]))
        print("\n\tResult inpace: ", rearrange_inplace(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()

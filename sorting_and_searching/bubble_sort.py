def bubble_sort(nums):

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    lst = [3, 2, 1, 5, 4]
    bubble_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)

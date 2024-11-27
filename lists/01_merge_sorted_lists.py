"""
Given two integer lists, nums1 and nums2, of size m and n, respectively, sorted in nondecreasing order. Merge
nums1 and nums2 into a single list sorted in nondecreasing order.


"""


def merge_lists(nums1, nums2):
    res = []
    j = 0
    print(len(nums1))
    print(len(nums2))
    for i in range(0, len(nums1)):
        ele1 = nums1[i]

        if j < len(nums2):
            while nums2[j] <= ele1:
                res.append(nums2[j])
                print(f"adding {nums2[j]} from nums2")
                j = j + 1
                print(f"new j {j}")
                if j >= len(nums2):
                    break

        res.append(ele1)
        print(f"adding {ele1}")

    while j < len(nums2):
        res.append(nums2[j])
        j = j + 1
    return res


merge_lists([10, 49, 99, 110, 176], [1, 2, 4, 7, 8, 12, 15, 19, 24, 50, 69, 80, 100])

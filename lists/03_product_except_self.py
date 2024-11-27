"""
You’re given an integer array, nums. Return a resultant array product so that product[i] is equal to the product of all the elements of nums except nums[i].

Write an algorithm that runs in O(n) time without using the division operation
"""


def find_product(nums):
    num_z = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            num_z += 1

    print(f"Number of zeros {num_z}")
    res = [0] * len(nums)
    if num_z > 1:
        return res

    elif num_z == 1:
        product = 1
        index = -1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                index = i
            else:
                product = product * nums[i]

        res[index] = product

    else:
        product = 1
        for i in range(0, len(nums)):
            product = product * nums[i]
        for i in range(0, len(nums)):
            res[i] = int(product / nums[i])

    return res


def find_product_without_division(nums):
    left = 1
    product = []
    # First pass: Calculate products starting from left
    for values in nums:
        product.append(left)
        left = left * values

    # Second pass: Update the product list by calculating products from right to left
    right = 1
    for i in range(len(nums) - 1, -1, -1):
        product[i] = product[i] * right
        right = right * nums[i]

    return product


print(find_product_without_division([2, 4, 0, 6]))
print("**************")
print(find_product_without_division([2, 4, 0, 0, 6]))
print("**************")
print(find_product_without_division([2, 4, 1, 7, 6]))

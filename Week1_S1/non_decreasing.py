"""
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example:

input:
nums = [4, 2, 3]
output:
non_decreasing(nums) -> True

input:
nums = [4, 2, 1]
output:
non_decreasing(nums) -> False

"""

def non_decreasing(nums):

    count = 0

    for i in range(len(nums)-1):

        if (nums[i] > nums[i+1]):
            count += 1
            if (count > 1):
                return False

    return True

nums1 = [4, 2, 3]
print(non_decreasing(nums1))

nums2 = [4, 2, 1]
print(non_decreasing(nums2))
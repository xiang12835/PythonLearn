# coding=utf-8

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 1:

Input: [1,3,5,6], 0
Output: 0
"""


# 对于排好序的数组进行插入的问题，为了减小算法的时间复杂度，很容易想到用二分查找的方法：


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return left

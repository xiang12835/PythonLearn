"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000

"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            r = max(r, count)
        return r


class Solution1(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        counter = 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                r = max(r, counter)
                counter = 0

        return max(r, counter)

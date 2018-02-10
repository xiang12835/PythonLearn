# coding=utf-8

"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.
Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""
import collections

"""
如果k大于0，则返回两个set的交集
如果k=0，则计数，找出出现1次以上的元素的个数
如果k小于0，返回0
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(nums) & set(n+k for n in nums))
        elif k == 0:
            l = collections.Counter(nums).values()
            count = 0
            for v in l:
                if v>1:
                    count += 1
            return count
            # return sum(v > 1 for v in collections.Counter(nums).values())
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    print s.findPairs([1, 3, 1, 5, 4], 0)

    print s.findPairs([1, 2, 3, 4, 5], 1)

    print s.findPairs([3, 1, 4, 1, 5], 2)

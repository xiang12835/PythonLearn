class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []

        length = len(nums)

        for i in xrange(length):
            for j in xrange(i+1, length):
                if nums[i] + nums[j] == target:
                    r = [i, j]
                    break

        return r


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []

        d = {}
        for idx, val in enumerate(nums):
            if target - val in d.keys():
                return [d[target-val], idx]
            else:
                d[val] = idx

        return r


if __name__ == "__main__":
    s = Solution()
    print s.twoSum([3, 2, 4], 6)

    s1 = Solution1()
    print s1.twoSum([3, 2, 4], 6)
# coding=utf-8

"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = '{0:032b}'.format(n)
        return b.count("1")


class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = bin(n)
        return bin_str.count("1")


class Solution3(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        """

        count = 0
        a = 1

        for i in range(32):
            if n & a:
                count += 1
            a = a << 1
        return count


class Solution4(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        """

        count = 0
        while n:
            count += 1
            n = n & (n - 1)

        return count

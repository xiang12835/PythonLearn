"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = '{0:032b}'.format(n)
        return int(b[::-1], 2)

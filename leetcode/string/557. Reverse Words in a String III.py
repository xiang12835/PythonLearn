"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        for word in s.split(" "):
            l.append(word[::-1])
        return " ".join(l)




class Solution1:
    def reverseWords(self, s):
        return ' '.join(s.split(' ')[::-1])[::-1]


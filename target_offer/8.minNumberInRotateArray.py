# coding=utf-8


""" 题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


""" 思路解析
从头到尾两两相邻元素进行比较进行，如果前面一个元素大于后面一个元素，则返回后面一个元素。如果从头到尾都没有满足条件的元素，则返回第一个元素。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        index = 1
        for i in xrange(len(rotateArray)):
            if rotateArray[i] > rotateArray[index]:
                return rotateArray[index]
            index += 1

        return rotateArray[0]


class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        for i in xrange(len(rotateArray)-1):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]

        return rotateArray[0]

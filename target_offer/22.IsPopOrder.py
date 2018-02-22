# coding=utf-8


"""问题描述

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

"""


"""思路解析

模拟两个栈的弹入弹出即可

"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            if stack and popV[0] == stack[-1]:
                popV.pop(0)
                stack.pop()
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    print s.IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 2, 1])

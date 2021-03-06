# coding=utf-8


""" 问题描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

""" 思路解析
一道典型的动态规划问题：
我们用f(n)表示跳上n级台阶的跳法。
可以看出，f(1)=1;f(2)=2。
那么，假设到了n级台阶，那么上一步就有两种情况，跳一步跟跳两步。
如果是跳一步跳上了n级台阶，那么他上一步在n-1级台阶，那么有多少种方法跳到n-1级呢，显然是f(n-1)，同理，如果跳两步，那么上一步在n-2级台阶，此时方法种数是f(n-2),所以总数是f(n)=f(n-1)+f(n-2)。

反向思考，但是编写代码的时候要正向求解，首先根据f(1)和f(2)计算出f(3),再根据f(2)和f(3)计算出f(4)…..一次类推计算出第n项。很容易理解这种思路的时间复杂度是O(n).
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1

        if number == 2:
            return 2

        l = [1, 2]
        for _ in xrange(3, number + 1):
            l.append(l[-2] + l[-1])
        return l[-1]


class Solution1:
    def jumpFloor(self, number):
        # write code here
        if number < 3:
            return number

        first = 1
        second = 2

        r = 0
        for _ in xrange(3, number + 1):
            r = first + second
            first = second
            second = r
        return r

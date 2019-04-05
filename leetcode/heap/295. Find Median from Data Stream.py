# coding=utf-8

"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

"""


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.

        两个堆，一个放更大的那一半数字，一个放更小的那一半数字

        """
        self.max_heap = []  # 可能会多一个数字
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        from heapq import heappush, heappop, heappushpop

        if len(self.max_heap) == len(self.min_heap):
            data = -heappushpop(self.min_heap, -num)
            heappush(self.max_heap, data)
        else:
            data = heappushpop(self.max_heap, num)
            heappush(self.min_heap, -data)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.min_heap[0] + self.max_heap[0]) / 2.0
        else:
            return self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

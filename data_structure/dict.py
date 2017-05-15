# coding=utf-8

'''
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

1) 查找和插入的速度极快，不会随着key的增加而变慢；
2) 需要占用大量的内存，内存浪费多。
而list相反：

1) 查找和插入的时间随着元素的增加而增加；
2) 占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print 'Thomas' in d # key不存在的错误，有两种办法，一是通过in判断key是否存在

print d.get('Thomas')  # 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print d.get('Thomas', -1)


# dict():
print dict(a=1, b=2)


# 当key缺失时，执行DefaultDict类，字典的实例将自动实例化这个数列
class DefaultDict(dict):
    def __missing__(self, key):
        return []

d = DefaultDict()
d['florp'] = 127

# coding=utf-8

print "Hello {a}".format(a="Python")

print "Hello %s" % "Python"

print "Hello " + "Python"


# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
str = "this is string example....wow!!!"
sub = "i"
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow"
print "str.count(sub) : ", str.count(sub)


# 字符反转
s = "abcdefg"
print s[::-1]


s = "hello"
print sorted(s)


# 去重
s = 'aaabbc'
def deduplicate(s):
    r = []
    l = list(s)
    for v in l:
        if v in r:
            continue
        r.append(v)
    r = "".join(r)
    return r

print deduplicate(s)


"""

‘与“

C 语言中单引号代表一个字符，它实际对应于编译器所采用的字符集中的一个整数值。而双引号则表示字符串，默认以 '\0' 结尾。

"""





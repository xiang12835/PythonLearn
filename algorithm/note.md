# 算法分析

## 数学模型

### 1. 近似

N<sup>3</sup>/6-N<sup>2</sup>/2+N/3 \~ N<sup>3</sup>/6。使用 \~f(N) 来表示所有随着 N 的增大除以 f(N) 的结果趋近于 1 的函数。

### 2. 增长数量级

N<sup>3</sup>/6-N<sup>2</sup>/2+N/3 的增长数量级为 O(N<sup>3</sup>)。增长数量级将算法与它的实现隔离开来，一个算法的增长数量级为 O(N<sup>3</sup>) 与它是否用 Java 实现，是否运行于特定计算机上无关。

### 3. 内循环

执行最频繁的指令决定了程序执行的总时间，把这些指令称为程序的内循环。

### 4. 成本模型

使用成本模型来评估算法，例如数组的访问次数就是一种成本模型。


## ThreeSum

ThreeSum 用于统计一个数组中三元组的和为 0 的数量。

该算法的内循环为 if(a[i]+a[j]+a[k]==0) 语句，总共执行的次数为 N(N-1)(N-2) =  N<sup>3</sup>/6-N<sup>2</sup>/2+N/3，因此它的近似执行次数为 \~N<sup>3</sup>/6，增长数量级为 O(N<sup>3</sup>)。

<font size=4> **改进** </font></br>

通过将数组先排序，对两个元素求和，并用二分查找方法查找是否存在该和的相反数，如果存在，就说明存在三元组的和为 0。

该方法可以将 ThreeSum 算法增长数量级降低为 O(N<sup>2</sup>logN)。


## 递归的两个特点：调用自身,结束条件

## 时间复杂度：用来估计算法运行时间的一个式子(单位)

常见复杂度排序：

    O(1) < O(logn) < O(n) < O(nlogn) < O(n的平方) < O(n的平方 logn) < O(n的三次方)

```python

n = 100

print("HelloWorld")   # O(1)
for i in range(n):    # O(n的平方)
      for j in range(n):
          print("HelloWorld")
for i in range(n):    # O(n的平方)
    for j in range(n):
      print("HelloWorld")
while n > 1:          # O(log₂n)或O(logn) 一般写后面这个
      print(n)
      n = n // 2

```

 - 常量时间复杂度 - 布隆过滤器 / 哈希存储
 - 对数时间复杂度 - 折半查找（二分查找）
 - 线性时间复杂度 - 顺序查找 / 桶排序
 - 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
 - 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
 - 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
 - 几何级数时间复杂度 - 汉诺塔
 - 阶乘时间复杂度 - 旅行经销商问题 - NP

## 空间复杂度：算法占用内存看空间的的大小

## 常用算法：

- 穷举法：又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
- 贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
- 分治法：把一个复杂的问题分成两个或更多的相同或相似的子问题，再把子问题分成更小的子问题，直到可以直接求解的程度，最后将子问题的解进行合并得到原问题的解。
- 回溯法：回溯法又称为试探法，按选优条件向前搜索，当搜索到某一步发现原先选择并不优或达不到目标时，就退回一步重新选择。
- 动态规划：基本思想也是将待求解问题分解成若干个子问题，先求解并保存这些子问题的解，避免产生大量的重复运算。


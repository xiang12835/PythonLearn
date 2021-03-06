# -*- coding:utf-8 -*-

""" 题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

""" 思路解析
根据前序遍历的结果，对于输入的遍历序列，第一个数一定是根结点，那么我们去中序遍历的结果中找到该根节点，中序遍历结果中根结点左边的是左子树的节点，右边的是右子树的节点，这样很容易使用递归的思路实现二叉树的重建。
 """


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None

        root = TreeNode(pre[0])
        index = 0
        while index <= len(tin) - 1:
            if tin[index] == pre[0]:
                break
            index += 1
        root.left = self.reConstructBinaryTree(pre[1:index + 1], tin[:index])
        root.right = self.reConstructBinaryTree(pre[index + 1:], tin[index + 1:])
        return root


class Solution1:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return

        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos + 1], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])

        return root

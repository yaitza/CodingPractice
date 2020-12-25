#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-24 15:20"

'''
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：

1 ≤ k ≤ 二叉搜索树元素个数
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    # 中序遍历 左子树---> 根结点 ---> 右子树
    def toMiddleString(self):
        if not self.val:
            return
        if self.left:
            self.left.toMiddleString()
        print(str(self.val)+"->", end='')
        if self.right:
            self.right.toMiddleString()
    # 前序遍历 根结点 ---> 左子树 ---> 右子树
    def toFrontString(self):
        if not self:
            return
        print(str(self.val) + "->", end='')
        if self.left:
            self.left.toFrontString()
        if self.right:
            self.right.toFrontString()
    # 后序遍历 左子树 ---> 右子树 ---> 根结点
    def toBackString(self):
        if not self:
            return
        if self.left:
            self.left.toBackString()
        if self.right:
            self.right.toBackString()
        print(str(self.val) + "->", end='')




class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k = self.k -1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)


        self.k = k
        dfs(root)
        return self.res

if __name__ == "__main__":
    root = TreeNode(5)
    left1 = TreeNode(3)
    right1 = TreeNode(6)
    left2 = TreeNode(2)
    right2 = TreeNode(4)
    left3 = TreeNode(1)
    left2.left = left3
    left1.left = left2
    left1.right = right2
    root.left = left1
    root.right = right1
    print()
    root.toFrontString()
    print()
    root.toMiddleString()
    print()
    root.toBackString()
    ss = Solution()
    print()
    print(ss.kthLargest(root, 3))

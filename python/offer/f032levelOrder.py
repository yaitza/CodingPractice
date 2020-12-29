#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-26 13:45"

'''
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
 

提示：

节点总数 <= 1000
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.index = 0
        def toMiddle(root):
            if not root:
                return
            if result.__len__() > self.index:
                result[self.index].append(root.val)
            else:
                result.append([root.val])

            if root.left:
                self.index = self.index + 1
                toMiddle(root.left)
                self.index = self.index - 1
            if root.right:
                self.index = self.index + 1
                toMiddle(root.right)
                self.index = self.index - 1
        toMiddle(root)
        return result




if __name__=="__main__":
    root = TreeNode(1)
    left1 = TreeNode(2)
    right1 = TreeNode(3)
    left2 = TreeNode(4)
    right2 = TreeNode(5)
    left1.left = left2
    left1.right = right2
    root.left = left1
    root.right = right1

    ss = Solution()
    print(ss.levelOrder(root))

#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-21 15:43"

'''
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 

限制：

0 <= 节点个数 <= 1000
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None and (isinstance(root, TreeNode) and  not isinstance(root.right, TreeNode)):
            return TreeNode()
        if isinstance(root, TreeNode) and not isinstance(root.right, TreeNode):
            tn = TreeNode(root.val)
            if root.left:
                tn.right = root.left
            if root.right:
                tn.left = root.right
            return tn
        else:
            result = TreeNode(root.val)
            result.left = self.mirrorTree(root.right)
            result.right = self.mirrorTree(root.left)
        return result


node7 = TreeNode(7)
node7.left = 9
node7.right = 6

node2 = TreeNode(2)
node2.left = 3
node2.right = 1

node = TreeNode(4)
node.left = node7
node.right = node2
s = Solution()
print(s.mirrorTree(node))

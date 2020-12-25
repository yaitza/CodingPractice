#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-23 14:33"

'''
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def toString(self):
        if not self.next:
            print(str(self.val))
            return
        print(str(self.val) + "->", end='')
        tmp = self.next
        while tmp.next:
            print(str(tmp.val) + "->", end='')
            if isinstance(tmp.next, ListNode):
                tmp = tmp.next
        print(str(tmp.val))


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        tmp = head
        stack = list()
        while tmp.next:
            stack.append(tmp.val)
            if isinstance(tmp.next, ListNode):
                tmp = tmp.next
        stack.append(tmp.val)
        nodes = []
        for i in stack[::-1]:
            nodes.append(ListNode(i))

        for node in nodes:
            if nodes.index(node) + 1 < len(nodes):
                node.next = nodes[nodes.index(node) + 1]
        return nodes[0]

    def reverseListEx(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        cur = head
        while head.next:
            tmp = head.next.next
            head.next.next = cur
            cur = head.next
            head.next = tmp
            head.toString()
            cur.toString()
        return cur

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node5.next = node6
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    node1.toString()
    ss = Solution()
    ss.reverseListEx(node1).toString()

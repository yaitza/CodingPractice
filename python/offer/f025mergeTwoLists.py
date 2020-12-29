#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-24 16:56"

'''
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return ListNode()

        middle_result = []
        while l1 or l2:
            if not l1 and l2:
                middle_result.append(ListNode(l2.val))
                l2 = l2.next
            if l1 and not l2:
                middle_result.append(ListNode(l1.val))
                l1 = l1.next
            if (l1 and l2) and (l1.val < l2.val):
                middle_result.append(ListNode(l1.val))
                l1 = l1.next
            if (l1 and l2) and (l1.val >= l2.val):
                middle_result.append(ListNode(l2.val))
                l2 = l2.next

        for node in middle_result:
            if middle_result.index(node) + 1 < len(middle_result):
                node.next = middle_result[middle_result.index(node) + 1]

        return middle_result[0]

    def mergeTwoListsEx(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dum = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next


if __name__ == "__main__":
    l14 = ListNode(4)
    l13 = ListNode(3)
    l13.next = l14
    l1 = ListNode(1)
    l1.next = l13

    l24 = ListNode(4)
    l22 = ListNode(2)
    l22.next = l24
    l2 = ListNode(1)
    l2.next = l22

    l1.toString()
    l2.toString()

    ss = Solution()
    ss.mergeTwoLists(l1, l2).toString()
    ss.mergeTwoListsEx(l1, l2).toString()





#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-22 16:20"

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
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
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
        for i in stack[len(stack)-k:]:
            nodes.append(ListNode(i))

        for node in nodes:
            node.toString()
            if nodes.index(node) + 1 < len(nodes):
                node.next = nodes[nodes.index(node) + 1]
                node.toString()
        return nodes[0]

    def getKthFromEndEx(self, head, k):
        if not head:
            return head

        tmp = head
        stack = list()
        while tmp.next:
            stack.append(tmp)
            if isinstance(tmp.next, ListNode):
                tmp = tmp.next
        stack.append(tmp)

        return stack[len(stack)-k]


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

    # node1.toString()

    ss = Solution()
    result = ss.getKthFromEndEx(node1, 4)
    result.toString()

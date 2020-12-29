#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-25 10:29"


class SingleLinkList(object):
    def __init__(self, val):
        self.value = val
        self.next = None

    def len(self):
        count = 0
        count_node = self
        while count_node:
            count += 1
            count_node = count_node.next
        return count

    def toPrint(self):
        """
        Print The Single Link
        :rtype: None
        """
        show_node = self
        while show_node:
            if show_node.next:
                print(show_node.value, end='->')
            else:
                print(show_node.value)
            show_node = show_node.next

    def front_insert_node(self, value):
        current_node = self
        new_node = SingleLinkList(value)
        new_node.next = current_node
        return new_node

    def back_insert_node(self, value):
        current_node = self
        new_node = SingleLinkList(value)
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


if __name__ == "__main__":
    l14 = SingleLinkList(4)
    l13 = SingleLinkList(3)
    l13.next = l14
    l1 = SingleLinkList(1)
    l1.next = l13

    l1.toPrint()

    l2 = l1.front_insert_node(0)
    l2.toPrint()
    l2.back_insert_node(5)
    l2.toPrint()

    node = SingleLinkList(0)
    for i in range(10):
        node.back_insert_node(i)
    node.toPrint()
    print(node.next.len())

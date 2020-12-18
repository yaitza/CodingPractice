#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================
from unittest import TestCase
from python.sample.l016threeSumClosest import *
__author__ = "yaitza"
__date__ = "2020-12-18 11:00"


class TestThreeSumClosest(TestCase):
    def test_threeSumClosest_1(self):
        self.assertEqual(threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_threeSumClosest_2(self):
        self.assertEqual(threeSumClosest([1, 1, 1, 1], 0), 3)

    def test_threeSumClosest_3(self):
        self.assertEqual(threeSumClosest([-100, -98, -2, -1], -101), 2)

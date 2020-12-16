#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-16 10:13"

import unittest
from python.sample.l003triangleminimumpath import *


class l003triangleminimumpathTest(unittest.TestCase):
    def test_get_minimum(self):
        self.assertEqual(1, triangle_min_path([1, 4, 5, 6]))

    def test_triangle_min_path(self):
        self.assertEqual(11, triangle_min_path([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

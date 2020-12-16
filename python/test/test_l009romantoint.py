#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

__author__ = "yaitza"
__date__ = "2020-12-15 15:32"

import unittest
from python.sample.l009romantoint import *

class l009romantointtest(unittest.TestCase):
    def test_romantoin1(self):
        result = romantoint("III")
        self.assertEqual(result, 3)

    def test_romantoint2(self):
        result = romantoint("IV")
        self.assertEqual(result, 4)

    def test_romantoint3(self):
        result = romantoint("IX")
        self.assertEqual(result, 9)

    def test_romantoint4(self):
        result = romantoint("LVIII")
        self.assertEqual(result, 58)

    def test_romantoint5(self):
        result = romantoint("MCMXCIV")
        self.assertEqual(result, 1994)

    def test_inttoroman1(self):
        result = inttoroman(3)
        self.assertEqual(result, "III")

    def test_inttoroman2(self):
        result = inttoroman(9)
        self.assertEqual(result, "IX")

    def test_inttoroman3(self):
        result = inttoroman(58)
        self.assertEqual(result, "LVIII")

    def test_inttoroman3(self):
        result = inttoroman(1994)
        self.assertEqual(result, "MCMXCIV")

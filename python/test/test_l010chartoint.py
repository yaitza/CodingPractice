#!/usr/bin/python
# coding=utf-8
# Copyright 2020 yaitza. All Rights Reserved.
#
#     https://yaitza.github.io/
#
# My Code hope to usefull for you.
# ===================================================================

import unittest
from python.sample.l010chartoint import *

class l010chartointtest(unittest.TestCase):
    def test_chartoint1(self):
        self.assertEqual(42, char_to_int("42"))

    def test_chartoint2(self):
        self.assertEqual(-42, char_to_int("     -42"))

    def test_chartoint3(self):
        self.assertEqual(4193, char_to_int("4193 with words"))

    def test_chartoint4(self):
        self.assertEqual(0, char_to_int("words and 98733"))
        
    def test_chartoint5(self):
        self.assertEqual(-2147483648, char_to_int("-91283472332"))

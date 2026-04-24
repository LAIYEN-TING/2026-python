#!/usr/bin/env python3
import unittest
import sys
import os

# Ensure parent directory is in path to import solutions
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from uva948 import process_input as process_948
from uva10008 import process_input as process_10008
from uva10019 import process_input as process_10019
from uva10035 import process_input as process_10035
from uva10038 import process_input as process_10038

class TestWeek04Solutions(unittest.TestCase):
    
    def test_uva948_false_coin(self):
        # 測試案例：3個硬幣，1號是輕的
        input_text = "1\n3 2\n1 1 2\n<\n1 1 3\n<\n"
        # 1號跟2號比，1號輕；1號跟3號比，1號輕。所以1號是假幣。
        self.assertEqual(process_948(input_text), "1")

    def test_uva10008_cryptanalysis(self):
        input_text = "2\nABC abc\nZZz zzZ\n"
        expected = "Z 6\nA 2\nB 2\nC 2"
        self.assertEqual(process_10008(input_text), expected)

    def test_uva10019_hashmat(self):
        input_text = "10 12\n100 200\n"
        expected = "2\n100"
        self.assertEqual(process_10019(input_text), expected)

    def test_uva10035_primary_arithmetic(self):
        input_text = "123 456\n555 555\n123 594\n0 0\n"
        # 123+456: 無進位
        # 555+555: 3次進位
        # 123+594: 1次進位 (3+4=7, 2+9=11 carry 1, 1+5+1=7)
        expected = "No carry operation.\n3 carry operations.\n1 carry operation."
        self.assertEqual(process_10035(input_text), expected)

    def test_uva10038_jolly_jumpers(self):
        input_text = "4 1 4 2 3\n5 1 4 2 -1 6\n"
        expected = "Jolly\nNot jolly"
        self.assertEqual(process_10038(input_text), expected)

if __name__ == '__main__':
    unittest.main()

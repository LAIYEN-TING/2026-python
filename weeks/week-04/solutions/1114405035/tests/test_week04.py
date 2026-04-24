import unittest

from uva10008 import process_input as process_10008
from uva10019 import process_input as process_10019
from uva10035 import process_input as process_10035
from uva10038 import process_input as process_10038
from uva948 import process_input as process_948


class TestWeek04Solutions(unittest.TestCase):
    def test_uva10008_sample(self):
        input_text = '2\nABC abc\nZZz zzZ\n'
        expected = (
            'Z 6\n'
            'A 2\n'
            'B 2\n'
            'C 2'
        )
        self.assertEqual(process_10008(input_text), expected)

    def test_uva10019_absolute_difference(self):
        input_text = '1 10\n100 200\n2147483647 0\n'
        expected = '9\n100\n2147483647'
        self.assertEqual(process_10019(input_text), expected)

    def test_uva10035_no_carry(self):
        self.assertEqual(process_10035('123 456\n0 0\n'), 'No carry operation.')

    def test_uva10035_one_carry(self):
        self.assertEqual(process_10035('555 555\n0 0\n'), '3 carry operations.')

    def test_uva10035_sample(self):
        self.assertEqual(process_10035('123 456\n5 5\n0 0\n'), 'No carry operation.\n1 carry operation.')

    def test_uva10038_jolly(self):
        self.assertEqual(process_10038('4 1 4 2 3\n5 1 4 2 -1 6\n'), 'Jolly\nNot jolly')

    def test_uva948_simple(self):
        input_text = (
            '2\n'
            '3 2\n1 1 2\n<\n'
            '1 1 3\n<\n'
            '3 1\n1 2 3\n<\n'
        )
        self.assertEqual(process_948(input_text), '1\n\n0')


if __name__ == '__main__':
    unittest.main()

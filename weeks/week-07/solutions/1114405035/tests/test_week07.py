import unittest

from uva10062 import process_input as process_10062
from uva10071 import process_input as process_10071
from uva10093 import process_input as process_10093
from uva10101 import process_input as process_10101
from uva10170 import process_input as process_10170


class TestWeek07Solutions(unittest.TestCase):
    def test_uva10062_sample(self):
        input_text = '4\n0\n0\n1\n'
        expected = '4\n3\n1\n2'
        self.assertEqual(process_10062(input_text), expected)

    def test_uva10071_sample(self):
        input_text = '2\n0\n1\n'
        expected = '6'
        self.assertEqual(process_10071(input_text), expected)

    def test_uva10093_sample(self):
        input_text = '3 3\nPPP\nPPP\nPPP\n'
        expected = '3'
        self.assertEqual(process_10093(input_text), expected)

    def test_uva10101_no_solution(self):
        input_text = '1+1=3#\n'
        self.assertEqual(process_10101(input_text), 'No')

    def test_uva10170_sample(self):
        input_text = '4 10\n'
        expected = '6'
        self.assertEqual(process_10170(input_text), expected)


if __name__ == '__main__':
    unittest.main()

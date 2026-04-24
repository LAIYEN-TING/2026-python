import unittest

from task1_sequence_clean import dedupe_keep_order, even_numbers, parse_sequence, process_sequence


class TestTask1SequenceClean(unittest.TestCase):
    def test_parse_sequence_with_spaces(self):
        self.assertEqual(parse_sequence('5 3 5 2 9 2 8 3 1'), [5, 3, 5, 2, 9, 2, 8, 3, 1])

    def test_dedupe_keep_order(self):
        self.assertEqual(dedupe_keep_order([5, 3, 5, 2, 9, 2, 8, 3, 1]), [5, 3, 2, 9, 8, 1])

    def test_even_numbers_preserve_order(self):
        self.assertEqual(even_numbers([5, 3, 5, 2, 9, 2, 8, 3, 1]), [2, 2, 8])

    def test_process_sequence_full_output(self):
        expected = (
            'dedupe: 5 3 2 9 8 1\n'
            'asc: 1 2 2 3 3 5 5 8 9\n'
            'desc: 9 8 5 5 3 3 2 2 1\n'
            'evens: 2 2 8'
        )
        self.assertEqual(process_sequence('5 3 5 2 9 2 8 3 1'), expected)


if __name__ == '__main__':
    unittest.main()

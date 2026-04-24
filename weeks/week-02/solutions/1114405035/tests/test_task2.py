import unittest

from task2_student_ranking import parse_student_line, process_student_ranking, sort_students, top_k_students


class TestTask2StudentRanking(unittest.TestCase):
    def test_parse_student_line(self):
        self.assertEqual(parse_student_line('amy 88 20'), ('amy', 88, 20))

    def test_sort_students_with_ties(self):
        records = [
            ('amy', 88, 20),
            ('bob', 88, 19),
            ('zoe', 92, 21),
            ('ian', 88, 19),
        ]
        expected = [
            ('zoe', 92, 21),
            ('bob', 88, 19),
            ('ian', 88, 19),
            ('amy', 88, 20),
        ]
        self.assertEqual(sort_students(records), expected)

    def test_top_k_students(self):
        records = [
            ('amy', 88, 20),
            ('bob', 88, 19),
            ('zoe', 92, 21),
            ('ian', 88, 19),
        ]
        self.assertEqual(top_k_students(records, 2), [('zoe', 92, 21), ('bob', 88, 19)])

    def test_process_student_ranking_output(self):
        input_text = '6 3\namy 88 20\nbob 88 19\nzoe 92 21\nian 88 19\nleo 75 20\neva 92 20\n'
        expected = 'eva 92 20\nzoe 92 21\nbob 88 19'
        self.assertEqual(process_student_ranking(input_text), expected)


if __name__ == '__main__':
    unittest.main()

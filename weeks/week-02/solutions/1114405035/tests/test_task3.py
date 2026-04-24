import unittest

from task3_log_summary import process_log_summary, sort_user_counts, top_action, user_event_counts


class TestTask3LogSummary(unittest.TestCase):
    def test_user_event_counts(self):
        lines = [
            'alice login',
            'bob login',
            'alice view',
            'bob view',
            'bob logout',
        ]
        self.assertEqual(user_event_counts(lines), {'alice': 2, 'bob': 3})

    def test_sort_user_counts_order(self):
        counts = {'alice': 3, 'bob': 4, 'chris': 1}
        self.assertEqual(sort_user_counts(counts), [('bob', 4), ('alice', 3), ('chris', 1)])

    def test_top_action_with_tie(self):
        lines = [
            'alice login',
            'bob view',
            'alice logout',
            'bob login',
            'bob view',
            'alice view',
        ]
        self.assertEqual(top_action(lines), ('view', 3))

    def test_process_log_summary_full_output(self):
        input_text = (
            '8\n'
            'alice login\n'
            'bob login\n'
            'alice view\n'
            'alice logout\n'
            'bob view\n'
            'bob view\n'
            'chris login\n'
            'bob logout\n'
        )
        expected = (
            'bob 4\n'
            'alice 3\n'
            'chris 1\n'
            'top_action: login 3'
        )
        self.assertEqual(process_log_summary(input_text), expected)


if __name__ == '__main__':
    unittest.main()

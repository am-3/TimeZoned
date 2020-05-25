import unittest
from datetime import time, timedelta

from t77_date.time import diff_time


class DiffTimeTestCase(unittest.TestCase):
    def test_null_params(self):
        self.assertIsNone(diff_time(None, None))
        self.assertIsNone(diff_time(time(), None))
        self.assertIsNone(diff_time(None, time()))

    def test_unknown_params(self):
        with self.assertRaises(ValueError):
            diff_time(time(), '')
        with self.assertRaises(ValueError):
            diff_time('', time())

    def test_diff(self):
        t1, t2 = time(hour=1), time(hour=2)

        self.assertEqual(diff_time(t2, t1), timedelta(hours=1))
        self.assertEqual(diff_time(t1, t2), timedelta(hours=-1))

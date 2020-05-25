import unittest
from datetime import timedelta

from t77_date import timedelta_to_str


class TimedeltaToStrTestCase(unittest.TestCase):
    def test_not_timedelta(self):
        """timedelta_to_str throw TypeError when val is not datetime.timedelta"""
        val = 'not timedelta object'
        with self.assertRaises(TypeError):
            timedelta_to_str(val)
        with self.assertRaises(TypeError):
            timedelta_to_str(val, True)

    def test_none(self):
        """timedelta_to_str return None for None input"""
        self.assertIsNone(timedelta_to_str(None))
        self.assertIsNone(timedelta_to_str(None, with_microseconds=True))

    def test_seconds(self):
        """timedelta_to_str return proper value of 1 second"""
        val = timedelta(seconds=1, microseconds=1)
        self.assertEqual(timedelta_to_str(val), '00:00:01')
        self.assertEqual(timedelta_to_str(val, with_microseconds=True), '00:00:01.000001')

    def test_1_day(self):
        """timedelta_to_str return proper value of 1 day"""
        val = timedelta(days=1, microseconds=1)
        self.assertEqual(timedelta_to_str(val), '24:00:00')
        self.assertEqual(timedelta_to_str(val, with_microseconds=True), '24:00:00.000001')

    def test_5_days(self):
        """timedelta_to_str return proper value of 5 days"""
        val = timedelta(days=5, microseconds=1)
        self.assertEqual(timedelta_to_str(val), '120:00:00')
        self.assertEqual(timedelta_to_str(val, with_microseconds=True), '120:00:00.000001')

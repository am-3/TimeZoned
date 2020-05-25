import unittest
from datetime import timedelta

from t77_date import timedelta_to_seconds


class TimedeltaToSecondsTestCase(unittest.TestCase):
    def test_not_timedelta(self):
        """timedelta_to_seconds throw TypeError when val is not datetime.timedelta"""
        val = 'not timedelta object'
        with self.assertRaises(TypeError):
            timedelta_to_seconds(val)
        with self.assertRaises(TypeError):
            timedelta_to_seconds(val, True)

    def test_none(self):
        """timedelta_to_seconds return None for None input"""
        self.assertIsNone(timedelta_to_seconds(None))
        self.assertIsNone(timedelta_to_seconds(None, with_microseconds=True))

    def test_1_second(self):
        """timedelta_to_seconds return proper value of 1 second"""
        val = timedelta(seconds=1, microseconds=1)
        self.assertEqual(timedelta_to_seconds(val), 1)
        self.assertEqual(timedelta_to_seconds(val, with_microseconds=True), 1.000001)

    def test_1_day(self):
        """timedelta_to_seconds return proper value of 1 day"""
        val = timedelta(days=1, microseconds=1)
        self.assertEqual(timedelta_to_seconds(val), 86400)
        self.assertEqual(timedelta_to_seconds(val, with_microseconds=True), 86400.000001)

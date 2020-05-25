import unittest
from datetime import timedelta, datetime

from t77_date import parse_timedelta


class ParseTimedeltaTestCase(unittest.TestCase):
    def test_none(self):
        """parse_timedelta return None for None input"""
        self.assertIsNone(parse_timedelta(None))

    def test_not_str(self):
        """parse_timedelta throw TypeError when value is not str"""
        for invalid in [[], {}, object(), 12, datetime.now()]:
            with self.assertRaises(TypeError):
                parse_timedelta(invalid)

    def test_incorrect(self):
        """parse_timedelta throw ValueError when value is invalid timedelta"""
        for invalid in ['invalid timedelta']:
            with self.assertRaises(ValueError):
                parse_timedelta(invalid)

    def test_hours_wo_day(self):
        data = {
            '1:11:12': timedelta(hours=1, minutes=11, seconds=12),
            '10:11:12': timedelta(hours=10, minutes=11, seconds=12),
            '25:11:12': timedelta(days=1, hours=1, minutes=11, seconds=12),
        }
        for val, expected in data.items():
            self.assertEqual(parse_timedelta(val), expected)

    def test_hours_and_days(self):
        data = {
            '1 day, 10:11:12': timedelta(days=1, hours=10, minutes=11, seconds=12),
            '2 days, 10:11:12': timedelta(days=2, hours=10, minutes=11, seconds=12),
        }
        for val, expected in data.items():
            self.assertEqual(parse_timedelta(val), expected)

    def test_microseconds(self):
        data = {
            '1:11:12.13': timedelta(hours=1, minutes=11, seconds=12, microseconds=13),
            '1 day, 10:11:12.13': timedelta(days=1, hours=10, minutes=11, seconds=12, microseconds=13),
        }
        for val, expected in data.items():
            self.assertEqual(parse_timedelta(val), expected)

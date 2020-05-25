import unittest
from datetime import datetime, date

from t77_date import end_of_day


class EndOfDayTestCase(unittest.TestCase):
    def test_new_object(self):
        """end_of_day create a new object"""
        now = datetime.now()
        eod = end_of_day(now)
        self.assertNotEqual(now, eod)

    def test_now(self):
        """Ending of day at 23:59:59.999999"""
        now = datetime.now()
        eod = end_of_day(now)
        self.assertEqual(eod, datetime(now.year, now.month, now.day, 23, 59, 59, 999999))

    def test_date(self):
        now = date.today()
        eod = end_of_day(now)
        self.assertEqual(eod, datetime(now.year, now.month, now.day, 23, 59, 59, 999999))

import unittest
from datetime import datetime, date

from t77_date import start_of_day


class StartOfDayTestCase(unittest.TestCase):
    def test_new_object(self):
        """start_of_day create a new object"""
        now = datetime.now()
        sod = start_of_day(now)
        self.assertNotEqual(now, sod)

    def test_now(self):
        """Beginning of day at 00:00:00"""
        now = datetime.now()
        sod = start_of_day(now)
        self.assertEqual(sod, datetime(now.year, now.month, now.day))

    def test_date(self):
        now = date.today()
        sod = start_of_day(now)
        self.assertEqual(sod, datetime(now.year, now.month, now.day))

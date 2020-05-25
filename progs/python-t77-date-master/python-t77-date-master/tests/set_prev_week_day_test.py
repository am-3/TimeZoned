import unittest
from datetime import datetime, date

from t77_date import FRIDAY, ISO_FRIDAY, set_prev_week_day


class SetPrevWeekDayTestCase(unittest.TestCase):
    def test_date_saturday_to_prev_friday(self):
        saturday = date(2016, 7, 2)  # SATURDAY
        prev_friday = set_prev_week_day(saturday, FRIDAY)
        self.assertEqual(prev_friday.weekday(), FRIDAY)
        self.assertLess(prev_friday, saturday)

    def test_date_friday_to_friday(self):
        friday = date(2016, 7, 1)  # FRIDAY
        prev_friday = set_prev_week_day(friday, FRIDAY)
        self.assertEqual(prev_friday.weekday(), FRIDAY)
        self.assertEqual(prev_friday, friday)

    def test_date_thursday_to_prev_friday(self):
        thursday = date(2016, 6, 30)  # THURSDAY
        prev_friday = set_prev_week_day(thursday, FRIDAY)
        self.assertEqual(prev_friday.weekday(), FRIDAY)
        self.assertLess(prev_friday, thursday)

    def test_datetime_saturday_to_prev_friday(self):
        saturday = datetime(2016, 7, 2, 12)  # SATURDAY
        prev_friday = set_prev_week_day(saturday, FRIDAY)
        self.assertEqual(prev_friday.weekday(), FRIDAY)
        self.assertLess(prev_friday, saturday)

    def test_datetime_friday_to_friday(self):
        friday = datetime(2016, 7, 1, 12)  # FRIDAY
        prev_friday = set_prev_week_day(friday, FRIDAY)
        self.assertEqual(prev_friday.weekday(), FRIDAY)
        self.assertEqual(prev_friday, friday)

    def test_datetime_thursday_to_prev_friday(self):
        thursday = datetime(2016, 6, 30, 12)  # THURSDAY
        prev_friday = set_prev_week_day(thursday, FRIDAY)
        self.assertEqual(prev_friday.weekday(), FRIDAY)
        self.assertLess(prev_friday, thursday)

    def test_date_saturday_to_prev_friday_iso(self):
        saturday = date(2016, 7, 2)  # SATURDAY
        prev_friday = set_prev_week_day(saturday, ISO_FRIDAY, True)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, saturday)

    def test_date_friday_to_friday_iso(self):
        friday = date(2016, 7, 1)  # FRIDAY
        prev_friday = set_prev_week_day(friday, ISO_FRIDAY, True)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertEqual(prev_friday, friday)

    def test_date_thursday_to_prev_friday_iso(self):
        thursday = date(2016, 6, 30)  # THURSDAY
        prev_friday = set_prev_week_day(thursday, ISO_FRIDAY, True)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, thursday)

    def test_datetime_saturday_to_prev_friday_iso(self):
        saturday = datetime(2016, 7, 2, 12)  # SATURDAY
        prev_friday = set_prev_week_day(saturday, ISO_FRIDAY, True)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, saturday)

    def test_datetime_friday_to_friday_iso(self):
        friday = datetime(2016, 7, 1, 12)  # FRIDAY
        prev_friday = set_prev_week_day(friday, ISO_FRIDAY, True)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertEqual(prev_friday, friday)

    def test_datetime_thursday_to_prev_friday_iso(self):
        thursday = datetime(2016, 6, 30, 12)  # THURSDAY
        prev_friday = set_prev_week_day(thursday, ISO_FRIDAY, True)
        self.assertEqual(prev_friday.isoweekday(), ISO_FRIDAY)
        self.assertLess(prev_friday, thursday)

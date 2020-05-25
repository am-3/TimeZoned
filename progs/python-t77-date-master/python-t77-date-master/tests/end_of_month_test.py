import unittest
from datetime import datetime, date

from t77_date import end_of_month


class EndOfMonthTestCase(unittest.TestCase):
    def test_new_object(self):
        """end_of_month create a new object"""
        now = datetime.now()
        eom = end_of_month(now)
        self.assertNotEqual(now, eom)

    def test_january(self):
        """Ending of january at 23:59:59.999999 31st day"""
        january = datetime(2015, 1, 6, 12, 45, 23, 123)
        eom = end_of_month(january)
        self.assertEqual(eom, datetime(2015, 1, 31, 23, 59, 59, 999999))

    def test_february(self):
        """Ending of february at 23:59:59.999999 28th day"""
        february = datetime(2015, 2, 6, 12, 45, 23, 123)
        eom = end_of_month(february)
        self.assertEqual(eom, datetime(2015, 2, 28, 23, 59, 59, 999999))

    def test_february_leap(self):
        """Ending of february in leap-year at 23:59:59.999999 29th day"""
        february = datetime(2000, 2, 6, 12, 45, 23, 123)
        eom = end_of_month(february)
        self.assertEqual(eom, datetime(2000, 2, 29, 23, 59, 59, 999999))

    def test_march(self):
        """Ending of march at 23:59:59.999999 31st day"""
        march = datetime(2015, 3, 6, 12, 45, 23, 123)
        eom = end_of_month(march)
        self.assertEqual(eom, datetime(2015, 3, 31, 23, 59, 59, 999999))

    def test_april(self):
        """Ending of april at 23:59:59.999999 30th day"""
        april = datetime(2015, 4, 6, 12, 45, 23, 123)
        eom = end_of_month(april)
        self.assertEqual(eom, datetime(2015, 4, 30, 23, 59, 59, 999999))

    def test_may(self):
        """Ending of may at 23:59:59.999999 31st day"""
        may = datetime(2015, 5, 6, 12, 45, 23, 123)
        eom = end_of_month(may)
        self.assertEqual(eom, datetime(2015, 5, 31, 23, 59, 59, 999999))

    def test_june(self):
        """Ending of june at 23:59:59.999999 30th day"""
        june = datetime(2015, 6, 6, 12, 45, 23, 123)
        eom = end_of_month(june)
        self.assertEqual(eom, datetime(2015, 6, 30, 23, 59, 59, 999999))

    def test_july(self):
        """Ending of july at 23:59:59.999999 31st day"""
        july = datetime(2015, 7, 6, 12, 45, 23, 123)
        eom = end_of_month(july)
        self.assertEqual(eom, datetime(2015, 7, 31, 23, 59, 59, 999999))

    def test_august(self):
        """Ending of august at 23:59:59.999999 31st day"""
        august = datetime(2015, 8, 6, 12, 45, 23, 123)
        eom = end_of_month(august)
        self.assertEqual(eom, datetime(2015, 8, 31, 23, 59, 59, 999999))

    def test_september(self):
        """Ending of september at 23:59:59.999999 30th day"""
        september = datetime(2015, 9, 6, 12, 45, 23, 123)
        eom = end_of_month(september)
        self.assertEqual(eom, datetime(2015, 9, 30, 23, 59, 59, 999999))

    def test_october(self):
        """Ending of october at 23:59:59.999999 31st day"""
        october = datetime(2015, 10, 6, 12, 45, 23, 123)
        eom = end_of_month(october)
        self.assertEqual(eom, datetime(2015, 10, 31, 23, 59, 59, 999999))

    def test_november(self):
        """Ending of november at 23:59:59.999999 30th day"""
        november = datetime(2015, 11, 6, 12, 45, 23, 123)
        eom = end_of_month(november)
        self.assertEqual(eom, datetime(2015, 11, 30, 23, 59, 59, 999999))

    def test_december(self):
        """Ending of december at 23:59:59.999999 31st day"""
        december = datetime(2015, 12, 6, 12, 45, 23, 123)
        eom = end_of_month(december)
        self.assertEqual(eom, datetime(2015, 12, 31, 23, 59, 59, 999999))

    def test_date(self):
        now = date.today()
        eod = end_of_month(now)
        self.assertNotEqual(now, eod)

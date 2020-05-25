import unittest
from datetime import datetime

from dateutil.tz import tzutc, tzlocal

from t77_date.tz import to_local


class ToLocalTestCase(unittest.TestCase):
    def test_datetime_in_utc(self):
        value_in = datetime.now(tz=tzutc())
        value_out = to_local(value_in)
        self.assertIsInstance(value_out, datetime)
        self.assertEqual(value_out.tzinfo, tzlocal())

    def test_datetime_in_local(self):
        value_in = datetime.now(tz=tzlocal())
        value_out = to_local(value_in)
        self.assertIsInstance(value_out, datetime)
        self.assertEqual(value_out.tzinfo, tzlocal())
        self.assertEqual(value_out, value_in)

    def test_datetime_without_tzinfo(self):
        value_in = datetime.now()
        value_out = to_local(value_in)
        self.assertIsInstance(value_out, datetime)
        self.assertEqual(value_out.tzinfo, tzlocal())

    def test_invalid_input(self):
        now = datetime.now()
        with self.assertRaises(ValueError):
            to_local(None)
        with self.assertRaises(ValueError):
            to_local(now.toordinal())
        with self.assertRaises(ValueError):
            to_local(now.isoformat())

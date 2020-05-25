"""A set of dateutil.tz related functions"""
from __future__ import print_function, division

from datetime import datetime

from dateutil.tz import tzlocal, tzutc


def _convert(value, tzto, defaulttz):
    """Convert datetime.datetime object between timezones"""
    if not isinstance(value, datetime):
        raise ValueError('value must be a datetime.datetime object')

    if value.tzinfo is None:
        value = value.replace(tzinfo=defaulttz)

    return value.astimezone(tzto)


def to_local(value, defaulttz=None):
    """Convert datetime.datetime time to local time zone

    If value doesn't have tzinfo, then defaulttz is set.
    Default value of defaulttz is UTC.
    """
    if defaulttz is None:
        defaulttz = tzutc()
    return _convert(value, tzlocal(), defaulttz)


def to_utc(value, defaulttz=None):
    """Convert datetime.datetime time to UTC

    If value doesn't have tzinfo, then defaulttz is set.
    Default value of defaulttz is local time zone.
    """
    if defaulttz is None:
        defaulttz = tzlocal()
    return _convert(value, tzutc(), defaulttz)

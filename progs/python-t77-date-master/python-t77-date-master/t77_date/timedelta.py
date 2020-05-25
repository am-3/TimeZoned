"""A set of datetime.timedelta related functions"""
from __future__ import absolute_import, division

import re
from datetime import timedelta

import six

from .constants import MICROSECONDS_IN_SECOND, SECONDS_IN_DAY, \
    SECONDS_IN_HOUR, SECONDS_IN_MINUTE, HOURS_IN_DAY, INTERVAL_REGEX_STR

INTERVAL_REGEX = re.compile(INTERVAL_REGEX_STR, re.VERBOSE)


def timedelta_to_seconds(value, with_microseconds=False):
    """
    Convert datetime.timedelta to seconds
    :param value: timedelta to convert
    :type value: datetime.timedelta
    :param with_microseconds:
    :type with_microseconds: bool
    :return: seconds/seconds with microseconds or None if val is None
    :rtype: int/float/None
    :raise: TypeError when val is not timedelta
    """
    if value is None:
        return None

    if not isinstance(value, timedelta):
        raise TypeError('value must be a datetime.timedelta object')

    microseconds = value.microseconds / MICROSECONDS_IN_SECOND \
        if with_microseconds else 0

    return value.days * SECONDS_IN_DAY + value.seconds + microseconds


def timedelta_to_str(value, with_microseconds=False):
    """
    String representation of datetime.timedelta
    :param value: timedelta to convert
    :type value: datetime.timedelta
    :param with_microseconds:
    :type with_microseconds: bool
    :return: String representation of datetime.timedelta or None if val is None
    :rtype: string/None
    :raise: TypeError when val is not timedelta
    """
    if value is None:
        return None

    if not isinstance(value, timedelta):
        raise TypeError('value must be a datetime.timedelta object')

    hours, remainder = divmod(value.seconds, SECONDS_IN_HOUR)
    hours += value.days * HOURS_IN_DAY
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)

    if with_microseconds:
        return '%02d:%02d:%02d.%06d' % (hours, minutes, seconds,
                                        value.microseconds)
    else:
        return '%02d:%02d:%02d' % (hours, minutes, seconds)


def parse_timedelta(value):
    """
    Parses a string and return a datetime.timedelta.
    :param value: string to parse
    :type value: str
    :return: timedelta object or None if value is None
    :rtype: timedelta/None
    :raise: TypeError when value is not string
    :raise: ValueError when value is not proper timedelta string
    """
    if value is None:
        return None

    if not isinstance(value, six.string_types):
        raise TypeError('value must be a string type')

    match = INTERVAL_REGEX.search(value)

    if match:
        data = match.groupdict()
        return timedelta(**dict((key, int(data[key] or 0)) for key in data))
    else:
        raise ValueError("Value '%s' doesn't appear to be a valid timedelta "
                         "string" % value)

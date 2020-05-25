"""A set of datetime.time related functions"""
from __future__ import absolute_import

from datetime import datetime, time


def diff_time(t1, t2):
    """
    Calculates datetime.timedelta between two datetime.time values.
    :param t1: First time
    :type t1: datetime.time
    :param t2: Second time
    :type t2: datetime.time
    :return: Differences between t1 and t2 or None when t1 or t2 is None
    :rtype: datetime.timedelta/None
    :raise: ValueError when t1 or t2 is not datetime.time or None
    """
    if t1 is None or t2 is None:
        return None

    if not isinstance(t1, time):
        raise ValueError('"t1" must be a datetime.time')
    if not isinstance(t2, time):
        raise ValueError('"t2" must be a datetime.time')

    dt1 = datetime(1, 1, 1,
                   t1.hour, t1.minute, t1.second, t1.microsecond, t1.tzinfo)
    dt2 = datetime(1, 1, 1,
                   t2.hour, t2.minute, t2.second, t2.microsecond, t2.tzinfo)

    return dt1 - dt2

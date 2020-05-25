# PyEpoch Module
# Python module that converts timezones, sets time and calculates the number of seconds since the Unix epoch.
# 1.1
# Edvard Busck-Nielsen 2018, 2020
# GNU GPL v. 3.0

import pytz
import datetime


# Gets seconds since the UNIX Epoch takes a date and a timezone.
def epoch_sec(date, tz):
    pst = pytz.timezone(tz)
    epoch = pst.localize(datetime.datetime(1970, 1, 1))

    # Calculates epoch seconds.
    delta_time = (date - epoch).total_seconds()

    return delta_time


# Converts timezone takes a date and a timezone.
def timezone(date, tz):
    pst = pytz.timezone(tz)
    i = pst.localize(date)

    return i


# Converts timezone & sets time to get ex. Midnight Pacific Time.
def timezone_set(date, tz, h, m, s):
    pst = pytz.timezone(tz)
    result = pst.localize(datetime.datetime(date.year, date.month, date.day, h, m, s))

    return result


# Get's today's date
def today():
    return datetime.datetime.now()

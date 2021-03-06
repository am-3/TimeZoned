#!/usr/bin/env python

import pendulum
import re

people = [
    [ "Australia/Adelaide", "rusty" ],
    [ "Europe/Zurich", "cdecker" ],
    [ "Europe/Rome", "lawrence" ],
    [ "Atlantic/Madeira", "steven" ],
    [ "Europe/Rome", "alekos", 10, 18 ],
    [ "UTC", "apoelstra", 15, 24 ],
]

c_red = '\033[31m'
c_green = '\033[32m'
c_yellow = '\033[33m'
c_blue = '\033[34m'
c_magenta = '\033[35m'
c_cyan = '\033[36m'
c_reset = '\033[0m'

def fmt(d):
    if d is None:
        return ""
    return d.strftime("%a %F  %R")

def tfmt(d):
    if d is None:
        return ""
    return d.strftime("%R")

strip_color_pat = re.compile(r"""
    \x1b     # literal ESC
    \[       # literal [
    [;\d]*   # zero or more digits or semicolons
    [A-Za-z] # a letter
    """, re.VERBOSE).sub

def strip_color(s):
    return strip_color_pat("", s)

def work_range(tz, start_hour, end_hour):
    now   = pendulum.now(tz)
    tomorrow = now.hour > end_hour
    start = pendulum.tomorrow(tz) if tomorrow else pendulum.today(tz)
    end   = pendulum.tomorrow(tz) if tomorrow else pendulum.today(tz)

    add_start_hours = 0
    add_end_hours = 0

    if start_hour > 23:
        add_start_hours = start_hour - 23
        start_hour = 23

    if end_hour > 23:
        add_end_hours = end_hour - 23
        end_hour = 23

    start = start.set(hour=start_hour, minute=0)
    end = end.set(hour=end_hour, minute=0)

    start = start.add(hours=add_start_hours)
    end = end.add(hours=add_end_hours)

    return (start, end)


def main():
    rows = [["name", "time", "start", "end", "lstart", "lend"]]
    for person in people:
        tz       = pendulum.timezone(person[0])
        name     = person[1]
        start_hour = person[2] if len(person) > 2 else 9
        end_hour   = person[3] if len(person) > 3 else 17

        (start, end) = work_range(tz, start_hour, end_hour)

        now      = pendulum.now()
        theirs   = now.in_tz(tz)
        lstart   = start.in_tz('local')
        lend     = end.in_tz('local')

        tomorrow = start.day > theirs.day
        our_tomorrow = lstart.day > now.day

        is_weekend = start.day_of_week == 6 or start.day_of_week == 7
        outside_work_hours = now < start or now > end
        color = c_red   if outside_work_hours else ""
        reset = c_reset if outside_work_hours else ""

        def tfm(d,l=False):
            is_tomorrow = (l and our_tomorrow) or (not l and tomorrow)
            return tfmt(d) + ("t" if is_tomorrow else "")

        row = [name, color + fmt(theirs), tfm(start), tfm(end), tfm(lstart,l=True), tfm(lend,l=True) + reset]

        rows.append(row)

    pad = " " * 4
    widths = [max(map(lambda x: len(strip_color(x)), col)) for col in zip(*rows)]
    for row in rows:
        print(pad.join((val.ljust(width) for val, width in zip(row, widths))))


main()

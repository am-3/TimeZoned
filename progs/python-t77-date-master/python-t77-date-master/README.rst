python-t77-date
===============

.. image:: https://travis-ci.org/tomi77/python-t77-date.svg?branch=master
   :target: https://travis-ci.org/tomi77/python-t77-date
.. image:: https://coveralls.io/repos/github/tomi77/python-t77-date/badge.svg?branch=master
   :target: https://coveralls.io/github/tomi77/python-t77-date?branch=master
.. image:: https://codeclimate.com/github/tomi77/python-t77-date/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/python-t77-date
   :alt: Code Climate

A set of functions related with dates

Installation
------------

Install via ``pip``

.. sourcecode:: sh

   pip install t77_date

datetime module
---------------

A set of ``datetime.datetime`` and ``datetime.date`` related functions.

start_of_day
~~~~~~~~~~~~

Return a new ``datetime.datetime`` object with values that represent a start of a day.

Example

.. sourcecode:: python

   >>> dt = datetime(2016, 7, 2, 21, 49, 12)
   >>> sod = start_of_day(dt)
   >>> print(sod)
   2016-07-02 00:00:00

end_of_day
~~~~~~~~~~

Return a new ``datetime.datetime`` object with values that represent a end of a day.

Example

.. sourcecode:: python

   >>> dt = datetime(2016, 7, 2, 21, 49, 12)
   >>> eod = end_of_day(now)
   >>> print(eod)
   2016-07-02 23:59:59.999999

start_of_month
~~~~~~~~~~~~~~

Return a new ``datetime.datetime`` object with values that represent a start of a month.

Example

.. sourcecode:: python

   >>> dt = datetime(2016, 7, 2, 21, 49, 12)
   >>> som = start_of_month(dt)
   >>> print(som)
   2016-07-01 00:00:00

end_of_month
~~~~~~~~~~~~

Return a new ``datetime.datetime`` object with values that represent a end of a month.

Example

.. sourcecode:: python

   >>> dt = datetime(2016, 7, 2, 21, 49, 12)
   >>> eom = end_of_day(now)
   >>> print(eom)
   2016-07-31 23:59:59.999999

set_next_week_day
~~~~~~~~~~~~~~~~~

Set week day.
New date will be greater or equal than input date.

Example

.. sourcecode:: python

   >>> saturday = datetime(2016, 7, 2, 21, 49, 12)
   >>> next_friday = set_next_week_day(saturday, ISO_FRIDAY, iso=True)
   >>> print(next_friday)
   2016-07-08 21:49:12
   >>> next_friday = set_next_week_day(saturday, FRIDAY, iso=False)
   >>> print(next_friday)
   2016-07-08 21:49:12

set_prev_week_day
~~~~~~~~~~~~~~~~~

Set week day.
New date will be less or equal than input date.

Example

.. sourcecode:: python

   >>> saturday = datetime(2016, 7, 2, 12)
   >>> prev_friday = set_prev_week_day(saturday, ISO_FRIDAY, iso=True)
   >>> print(prev_friday)
   2016-07-01 21:49:12
   >>> prev_friday = set_prev_week_day(saturday, FRIDAY, iso=False)
   >>> print(prev_friday)
   2016-07-01 21:49:12

time module
-----------

A set of ``datetime.time`` related functions.

diff_time
~~~~~~~~~

Calculates ``datetime.timedelta`` between two ``datetime.time`` values.

Example

.. sourcecode:: python

   >>> t1, t2 = time(hour=1), time(hour=2)
   >>> print(diff_time(t2, t1))
   1:00:00
   >>> print(diff_time(t1, t2))
   -1 day, 23:00:00

timedelta module
----------------

A set of ``datetime.timedelta`` related functions.

timedelta_to_seconds
~~~~~~~~~~~~~~~~~~~~

Convert ``datetime.timedelta`` to seconds.

Example

.. sourcecode:: python

   >>> td = timedelta(days=1, microseconds=1)
   >>> seconds = timedelta_to_seconds(td)
   >>> print(seconds)
   86400
   >>> seconds = timedelta_to_seconds(td, with_microseconds=True)
   >>> print(seconds)
   86400.000001

timedelta_to_str
~~~~~~~~~~~~~~~~

String representation of ``datetime.timedelta``.

Example

.. sourcecode:: python

   >>> td = timedelta(days=5, microseconds=1)
   >>> td_str = timedelta_to_str(td)
   >>> print(td_str)
   '120:00:00'
   >>> td_str = timedelta_to_str(val, with_microseconds=True)
   >>> print(td_str)
   '120:00:00.000001'

parse_timedelta
~~~~~~~~~~~~~~~

Parses a string and return a ``datetime.timedelta``.

Example

.. sourcecode:: python

   >>> value = '1:11:12.13'
   >>> td = parse_timedelta(value)
   >>> print(td)
   1:11:12.000013
   >>> value = '1 day, 10:11:12.13'
   >>> td = parse_timedelta(value)
   >>> print(td)
   1 day, 1:11:12.000013

tz module
---------

A set of ``dateutil.tz`` related functions.

to_utc
~~~~~~

Convert ``datetime.datetime`` to UTC.

Example

.. sourcecode:: python

   >>> d1 = datetime.now(tz=tzlocal())
   >>> d2 = to_utc(d1)
   >>> print(d1)
   2017-02-20 13:19:36.511822+01:00
   >>> print(d2)
   2017-02-20 12:19:36.511822+00:00

to_local
~~~~~~~~

Convert ``datetime.datetime`` to local time zone.

Example

.. sourcecode:: python

   >>> d1 = datetime.now(tz=tzutc())
   >>> d2 = to_local(d1)
   >>> print(d1)
   2017-02-20 12:19:36.511822+00:00
   >>> print(d2)
   2017-02-20 13:19:36.511822+01:00

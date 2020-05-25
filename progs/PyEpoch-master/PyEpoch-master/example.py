# PyEpoch Module Example File.

import pyepoch

# -- TODAY() --

# The today() function returns today's date.
today = pyepoch.today()
print("Today's date & time:")
print(today)

# -- TIMEZONE() --

# The timezone() function returns a date with a different timezone.
# timezone() takes two(2) arguments:
#   - date = a date to be converted.
#   - tz = the timezone to convert to (ex. 'US/Pacific').

today_pst = pyepoch.timezone(today, 'US/Pacific')
print('Today\'s date & time in Pacific time:')
print(today_pst)

# -- TIMEZONE_SET() --

# The timezone_set() function returns a date with a different timezone and new hour/minute/second values.
# timezone_set() takes five(5) arguments:
#   - date = a date to be converted.
#   - tz = the timezone to convert to (ex. 'US/Pacific').
#   - h = hour, changes the hour of the output.
#   - m = minute, changes the minute of the output.
#   - s = second, changes the second(s) of the output.

time = pyepoch.timezone_set(today, 'US/Pacific', 8, 0, 0)
print('Today\'s date at 8 o\'clock Pacific time: ')
print(time)

# -- EPOCH_SEC() --

# The PyEpoch_sec() function returns the number of seconds since the UNIX epoch (1970, 1, 1) up to the provided date.
# timezone_set() takes two(2) arguments:
#   - date = a date to be converted.
#   - tz = the timezone as a string, (ex. 'US/Pacific').

sec = pyepoch.epoch_sec(today_pst, 'US/Pacific')
print('Todays\'s date & time in Pacific time as seconds since the Unix epoch: ')
print(sec)

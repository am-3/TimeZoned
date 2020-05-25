# PyEpoch
A Python module that converts timezones, sets time and calculates the number of seconds since the UNIX epoch.


# Installation

Download the epoch.py file and then import it into your python project.

```python
import pyepoch
```

<br>

# Basic usage

How to use PyEpoch.

```python
# Gets today's date.
today = pyepoch.today()
```

<br>

# Documentation

## Today()

### The today() function
Returns today's date using _datetime.datetime_

### Ex.

```python
# Gets today's date.
today = pyepoch.today()
>>> 2018, 11, 8, 11, 32, 59, 744692
```

<br>

## Epoch_Sec()


### The epoch_sec() function
Returns the number of seconds passed up to a specific date since the Unix epoch.
The function takes two parameters:
<br>
- A date: a datetime object
- A timezone: a timezone string, ex. 'US/Pacific'

### Ex.

```python
# Gets today's date.
today = pyepoch.today()
# Seconds up to today since the Unix epoch.
today = pyepoch.epoch_sec(today, 'US/Pacific')
>>> 2018, 11, 8, 11, 32, 59, 744692-08:00
```



## Timezone_Set()


### The timezone_set() function
Returns a passed in time into another timezone (also passed in) and sets the hour/minute/second in the passed in date.
The function takes five parameters:<br>
- A date: a datetime object to be converted.
- A timezone: a timezone string, ex. 'US/Pacific'
- Hour int
- Minute int
- Second int


### Ex.

```python
# Gets today's date.
today = pyepoch.today()
# Midnight pacific time today.
today = pyepoch.timezone(today, 'US/Pacific', 0, 0, 0)
>>> 2018-11-08 08:00:00-08:00
```

# Examples

You can download the 'example.py' file to see the functions in action.

# Contact
GitHub: <a href="https://github.com/buscedv" traget="blank">@Buscedv</a>
<br><br>
Edvard Busck-Nielsen 2020

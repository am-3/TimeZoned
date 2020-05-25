
# workhours

track work hours of colleagues in different timezones

## dependencies

  - pendulum (pip)

## customize

Edit the people array in the script. Columns are `timezone`, `name`, `start hour`, `end hour`

```python
people = [
    [ "Australia/Adelaide", "rusty" ],
    [ "Europe/Zurich", "cdecker" ],
    [ "Europe/Rome", "lawrence" ],
    [ "Atlantic/Madeira", "steven" ],
    [ "Europe/Rome", "alekos", 10, 18 ],
]
```


## example

- `t` means tomorrow
- `lstart` their start of work in your local time
- `lend` their end off work in your local time
- `t` in the local columns means *your* tomorrow. 
- `t` in the `start` and `end` columns is *their* tomorrow.

The row will be red if the current row is outside of work hours.

    name        time                     start     end       lstart    lend
    rusty       Sat 2019-11-09  05:56    09:00     17:00     14:30     22:30
    cdecker     Fri 2019-11-08  20:26    09:00t    17:00t    00:00t    08:00t
    lawrence    Fri 2019-11-08  20:26    09:00t    17:00t    00:00t    08:00t
    steven      Fri 2019-11-08  19:26    09:00t    17:00t    01:00t    09:00t
    alekos      Fri 2019-11-08  20:26    10:00t    18:00t    01:00t    09:00t

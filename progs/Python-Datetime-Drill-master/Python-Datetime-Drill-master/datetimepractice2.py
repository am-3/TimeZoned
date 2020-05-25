from datetime import datetime
from pytz import timezone

time_pdx = datetime.now(timezone('US/Pacific'))
print(time_pdx.strftime('%H:%M:%S %p'))

time_ny = datetime.now(timezone('US/Eastern'))
print(time_ny.strftime('%H:%M:%S %p'))

time_london = datetime.now(timezone('Europe/London'))
print(time_london.strftime('%H:%M:%S %p'))


if ('09:00:00') < time_pdx.strftime('%H:%M:%S %p') and \
   time_london.strftime('%H:%M:%S %p') < ('21:00:00'):
    print('Status:Portland Office Open')
else:
    print('Status:Portland Office Closed')


if ('09:00:00') < time_pdx.strftime('%H:%M:%S %p') and \
   time_london.strftime('%H:%M:%S %p') < ('21:00:00'):
    print('Status:New York Office Open')
else:
    print('Status:New York Office Closed')

if ('09:00:00') < time_pdx.strftime('%H:%M:%S %p') and \
   time_london.strftime('%H:%M:%S %p') < ('21:00:00'):
    print('Status:London Office Open')
else:
    print('Status:London Office Closed')
   





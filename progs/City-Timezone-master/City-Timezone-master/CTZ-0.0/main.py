import datetime
import time
import pytz
from city import City
import sys, os
import matplotlib
import matplotlib.pyplot as plt
from visualize import Vis

city_a = City()
city = city_a.read_city


#local tz = GMT+8
tz = pytz.timezone('Asia/Shanghai')

#get the time of the meeting
def get_time():
    try:
        #get start time
        time_s = input('The start time will be: YYYY/MM/DD HH:MM \n e.g. 2019/05/25 19:30\n')
        #format it
        time_s = datetime.datetime.strptime(time_s, "%Y/%m/%d %H:%M")
        #timezone = local time zone
        time_s = tz.localize(time_s)
        time_l = input('The meeting will last: HH:MM \n e.g. 2:30\n')
        time_l_hour, time_l_min = map(int,time_l.split(':'))
        return time_s, time_l_hour, time_l_min
        #print(time_s)
    except:
        print('Wrong! Try again plz.\n')
        get_time()



while True:
    time_start, time_last_hour, time_last_min = get_time()
    for key in city:
        t_s = str(time_start.astimezone(pytz.timezone(city[key])))
        t_e = str(time_start.astimezone(pytz.timezone(city[key]))+datetime.timedelta(hours=time_last_hour)+datetime.timedelta(minutes=time_last_min))
        print(key + ' : \n' + t_s + '\n---\n' + t_e + '\n')
    vis = Vis(city, time_start, time_last_hour, time_last_min)
    vis

    
    '''
    print(time_start, time_last_hour, time_last_min)
    print(time_start.tzinfo)
    print(time_start.astimezone(pytz.timezone("UTC")))
    '''

import sys, os
import matplotlib
import matplotlib.pyplot as plt
import datetime
import time
import pytz

class Vis():
    def __init__(self, city, time_start, time_last_hour, time_last_min):
        # new fig
        fig = plt.figure()
        # data
        city_list = []
        time_s = []
        time_e = []
        for key in city:
            city_list.append(key)
            ts = time_start.astimezone(pytz.timezone(city[key]))
            ts = float(ts.hour) + float(ts.minute)/60
            time_s.append(ts)
            te = time_start.astimezone(pytz.timezone(city[key]))+datetime.timedelta(hours=time_last_hour)+datetime.timedelta(minutes=time_last_min)
            te = float(te.hour) + float(te.minute)/60
            time_e.append(te)
        # draw pic
        l2=plt.barh(city_list, time_e, color='cyan')
        l1=plt.barh(city_list, time_s, color='w')
        """
        # set title
        plt.title("TIME")
        # set x，y label
        plt.xlabel('Time')
        plt.ylabel('City')
        """
        # set mark
        plt.xticks([x for x in range(0,24,1)])
        plt.yticks(city_list)
        tt = 0
        for city_list, city_list, time_s, time_e in zip(city_list, city_list, time_s, time_e):
            min_s = int((time_s % 1)*60)
            if min_s < 10:
                min_s = '0' + str(min_s)
            else:
                min_s = str(min_s)
            min_e = int((time_e % 1)*60)
            if min_e < 10:
                min_e = '0' + str(min_e)
            else:
                min_e = str(min_e)
            plt.text(time_s , tt-0.25, str(int(time_s)) + ":" + min_s, ha='center', va='bottom')
            plt.text(time_e , tt-0.25, str(int(time_e)) + ":" + min_e, ha='center', va='bottom')
            tt +=1
        # show
        plt.show()


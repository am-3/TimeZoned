import pendulum
import when
import datetime

hour = int(input("Provide the hours of the current time:"))
minute = int(input("Provide the minutes of the current time:"))

def DeepSearch():
    found = False
    i = 0
    for t in timezones:
        check_time = pendulum.now(t)
        if (check_time.hour == hour and minute < 60):
            i += 1
            print("Hit #{}: {} with time value of {}:{}".format(i,t,check_time.hour,check_time.minute))
            found = True

            if (found == False):
                print("Unable to find the specific local time even in deep search, feeling sorry for you.")



def QuickSearch():
    call = 'n'
    i = 0
    found = False
    for t in timezones:
        check_time = pendulum.now(t)
        if( check_time.minute == minute and check_time.hour == hour):
                i += 1
                print("Hit #{}: {}".format(i, t))
                found = True

    if(found == False):
        call = input("Unable to find the specific local time, do you want to continue with deep search? Y/N?")

    if(call == 'y' or call == 'Y'):
        DeepSearch()


timezones = when.all_timezones()
choice = int(input("1. Quick search (Searches for timezone based on accurate timing of minutes & hours)\n"
               "2. Deep search (Searches for timezones which are near requested local time"))
if(choice == 1):
    QuickSearch()
elif(choice == 2):
    DeepSearch()
else:
    print("Unknown command received!")


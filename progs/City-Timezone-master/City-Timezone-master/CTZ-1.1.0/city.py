"""
city = {
    'Hangzhou': 'Asia/Shanghai',
    'Bangalore' : 'Asia/Kolkata',
    'ESpoo' : 'Europe/Helsinki',
    'Wroclaw' : 'Europe/Warsaw',
    'Paris-Saclay' : 'Europe/Paris',
    'Timisoara' : 'Europe/Bucharest',
    'Arlington Heights' : 'America/Chicago',
    'Irving' : 'America/Chicago',
    'Naperville' : 'America/Chicago',
    'Ulm' : 'Europe/Berlin'
}
"""
import pytz

class City():
    def __init__(self):
        try:
            city_s = open('city_save.txt','r')
            t = city_s.read()
            self.read_city = eval(t)
            city_s.close()
        except:
            self.read_city = {
            'Hangzhou': 'Asia/Shanghai',
            'Bangalore' : 'Asia/Kolkata',
            'Timisoara' : 'Europe/Bucharest',
            'ESpoo' : 'Europe/Helsinki',
            'Wroclaw' : 'Europe/Warsaw',
            'Paris-Saclay' : 'Europe/Paris',
            'Ulm' : 'Europe/Berlin',
            'UTC' : 'UTC',
            'Arlington Heights' : 'America/Chicago',
            'Irving' : 'America/Chicago',
            'Naperville' : 'America/Chicago'
            }
'''
    def edit_city(self):
        print(self.read_city)
        print('\n')
        while True:
            try:
                temp = int(input('1.Search timezone by country\n2.See all of the timezone\n3.You alraedy kown the timezone\n4.Delete city\n5.exit\n'))
            except:
                continue
            if temp is 1:
                country = input('The city is in which country, \nplz using abbreviation, such as : us cn fl ,etc.\n')
                try:
                    print(str(pytz.country_timezones(country)))
                except:
                    print("Wrong, plz correct the abbreviation or using a nearby country's abbreviation \n")
                    continue
            elif temp is 2:
                print(pytz.all_timezones)
            elif temp is 3:
                pass
            elif temp is 4:
                print(self.read_city)
                tt = input("city's name\n")
                try:
                    self.read_city.pop(tt)
                    city_s = open('city_save.txt','w')
                    city_s.write(str(self.read_city))
                    city_s.close()
                    print(self.read_city)
                    continue
                except:
                    print('Wrong!Try again!\n')
                    continue
            elif temp is 5:
                break
            else:
                continue
            k = input("City's name\n")
            v = input("The timezone, e.g. Asia/Harbin \n")
            if v in pytz.all_timezones:
                self.read_city[k] = v
                city_s = open('city_save.txt','w')
                city_s.write(str(self.read_city))
                city_s.close()
                input('\nDone. Press Enter To Continue\n')
                continue
            else :
                print('Wrong!Try again!\n')
                continue



'''

#c = City()

#print(c.read_city)

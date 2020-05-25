import pygame
import sys
import os
from city import City
import datetime
import pytz

#time zone = utc+8
tz = pytz.timezone('Asia/Shanghai')

# e_w e_h 为单位格子宽 长
global e_w, e_h, mouse_x, mouse_y, bgc, line, city
global city_num, city_name, city_name_addition, t_e, t_s, day,time_day
global R,G,B,counter,color_temp
R = G = B = counter = color_temp = 0
#initial time == now
now = datetime.datetime.now()
day = datetime.date.today()
time_day = str(day.year)+'-'+str(day.month)+'-'+str(day.day)
t_s = 2*now.hour + now.minute//30 # K* 0.5 hour
t_e = 2*now.hour + now.minute//30 + 1
dic_tt={}
city_a = City()
city = city_a.read_city
city_num = len(city.keys())
city_name = []
city_name_addition = []
#multi-row display text
for k in city:
    while True:
        try:
            k1,k2 = k.split('')
            break
        except:
            pass
        try:
            k1,k2 = k.split('-')
            break
        except:
            pass
        try:
            k1,k2 = k[:10],k[10:]
            break
        except:
            k1 = k
            k2 = ''
    city_name.append(k1)
    city_name_addition.append(k2)

#bgc: backgroud color
bgc = (180,180,180)
#screen
screen_width = 960
screen_height = 480
screen_size = (screen_width,screen_height)
#line
line_color = (245,245,245)
line_width = 1
line = (line_color,line_width)

#put text
def drawText(screen,text,posx,posy,textHeight=32,fontColor=(255,255,255)):
    fontObj = pygame.font.SysFont("arial", 16)
    textSurfaceObj = fontObj.render(text, True,fontColor)  # 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (posx, posy)
    screen.blit(textSurfaceObj, textRectObj)


def check_events(screen, screen_size):
    global e_w, e_h, mouse_x, mouse_y, bgc, line
    global city_num, city_name, city_name_addition, now, t_e, t_s
    e_w, e_h = screen_width / (city_num+2), screen_height / 22
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            event_key(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_mouse(event, screen, screen_size)
        '''
        elif event.type == pygame.VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
            e_w, e_h = screen_width / 16, screen_height / 56
            pygame.display.update()
        '''
def event_mouse(event, screen, screen_size):
    global e_w, e_h, mouse_x, mouse_y, bgc, line, t_e, t_s, day, dic_tt, time_day
    global R,G,B,color_temp
    #y = []
    if event.button == 1 and e_w<mouse_x<2*e_w and 2*e_h<mouse_y:
        #y.append(mouse_y)
        y = mouse_y
        t_e = (y//e_h-1+16)#+1-2.-2是上面两行name
        t_s = (y//e_h-2+16)
        cal()
        vis(screen)
    elif 2<= event.button <=3 :
        pygame.init()
        #day = datetime.date.today()
        #time_day = str(day.year)+'-'+str(day.month)+'-'+str(day.day)
        R = G = B = color_temp= 0
        screen = pygame.display.set_mode(screen_size)
        screen.fill(bgc)
        pygame.display.flip()
        pygame.display.set_caption('City Time')
        e_w, e_h = screen_width / (city_num+2), screen_height / 22
        #pygame.draw.line(screen,color,(100,100),(500,400),width)
        draw(screen, screen_size, line, city)
        drawText(screen,time_day,e_w/2,e_h)
        pygame.display.update()
    #scroll wheel_up
    elif event.button == 4:
        day = day + datetime.timedelta(days=1)
        time_day = str(day.year)+'-'+str(day.month)+'-'+str(day.day)
        pygame.init()
        R = G = B = color_temp= 0
        screen = pygame.display.set_mode(screen_size)
        screen.fill(bgc)
        pygame.display.flip()
        pygame.display.set_caption('City Time')
        e_w, e_h = screen_width / (city_num+2), screen_height / 22
        #pygame.draw.line(screen,color,(100,100),(500,400),width)
        draw(screen, screen_size, line, city)
        drawText(screen,time_day,e_w/2,e_h)
        pygame.display.update()
    #scroll wheel_down
    elif event.button == 5:
        day = day - datetime.timedelta(days=1)
        time_day=str(day.year)+'-'+str(day.month)+'-'+str(day.day)
        pygame.init()
        R = G = B = color_temp= 0
        screen = pygame.display.set_mode(screen_size)
        screen.fill(bgc)
        pygame.display.flip()
        pygame.display.set_caption('City Time')
        e_w, e_h = screen_width / (city_num+2), screen_height / 22
        #pygame.draw.line(screen,color,(100,100),(500,400),width)
        draw(screen, screen_size, line, city)
        drawText(screen,time_day,e_w/2,e_h)
        pygame.display.update()


def event_key(event):
    global day,e_w,e_h,R,G,B,color_temp
    if event.key == pygame.K_q :
        sys.exit()
    elif event.key == pygame.K_r :
        pygame.init()
        day = datetime.date.today()
        time_day = str(day.year)+'-'+str(day.month)+'-'+str(day.day)
        R = G = B = color_temp= 0
        screen = pygame.display.set_mode(screen_size)
        screen.fill(bgc)
        pygame.display.flip()
        pygame.display.set_caption('City Time')
        e_w, e_h = screen_width / (city_num+2), screen_height / 22
        #pygame.draw.line(screen,color,(100,100),(500,400),width)
        draw(screen, screen_size, line, city)
        drawText(screen,time_day,e_w/2,e_h)
    pygame.display.update()


def draw(screen, screen_size, line, city):
    global city_num, city_name, city_name_addition, day, t_e, t_s
    for x in range(1,city_num+2):
        xx = x
        x = x*e_w
        pygame.draw.line(screen,line_color,(x,2*e_h),(x,screen_height),line_width)
        try:
            drawText(screen,city_name[xx-1],x+e_w/2,e_h/2) #screen text x y
            drawText(screen,city_name_addition[xx-1],x+e_w/2,3*e_h/2) #screen text x y
        except:
            pass
    for y in range(2,23):
        y = y*e_h
        pygame.draw.line(screen,line_color,(e_w,y),(screen_width-e_w,y),line_width)
    for i in range(8,18):
        drawText(screen,str(i)+':00',e_w/2,(i-7)*2*e_h) #screen text x y

def rect(screen,i,s_time,e_time):
    global R,G,B
    x = (1+i)*e_w
    y = (s_time + 2-16)*e_h
    h = abs(e_time - s_time)*e_h
    if y >= 2*e_h :
        pygame.draw.rect(screen, (R,G,B,30) ,(x,y,e_w,h))
        if int(s_time%2)*30 == 0 :
            time_text = str(int(s_time//2))+':'+'00'
        else:
            time_text = str(int(s_time//2))+':'+'30'
        drawText(screen, time_text ,x+e_w/2,y-e_h/2)
        if int(e_time%2)*30 == 0 :
            time_text = str(int(e_time//2))+':'+'00'
        else:
            time_text = str(int(e_time//2))+':'+'30'
        drawText(screen, time_text ,x+e_w/2,y+h-e_h/2)

def get_time():
    global day, t_e, t_s
    time_start=str(day.year)+'-'+str(day.month)+'-'+str(day.day)+'-'+str(int(t_s//2))+'-'+str(int(t_s%2)*30)
    time_start = datetime.datetime.strptime(time_start, "%Y-%m-%d-%H-%M")
    time_end=str(day.year)+'-'+str(day.month)+'-'+str(day.day)+'-'+str(int(t_e//2))+'-'+str(int(t_e%2)*30)
    time_end = datetime.datetime.strptime(time_end, "%Y-%m-%d-%H-%M")
    #time in list [Y,m,d,HH,MM]
    #time_in_list[3]
    return time_start, time_end

def cal():
    global city_num, city_name, city_name_addition, day, t_e, t_s, dic_tt
    time_start, time_end = get_time()
    for key in city:
        tt_s = time_start.astimezone(pytz.timezone(city[key]))
        tt_e = time_end.astimezone(pytz.timezone(city[key]))
        dic_tt[key] = (tt_s,tt_e)
        #print(key + ' : \n' + t_s + '\n---\n' + t_e + '\n')
    #print(dic_tt)

def vis(screen):
    global dic_tt, R, G, B, counter,color_temp
    i = 0 
    for key in dic_tt:
        city_s_hour = dic_tt[key][0].hour
        city_s_minute = dic_tt[key][0].minute
        city_e_hour = dic_tt[key][1].hour
        city_e_minute = dic_tt[key][1].minute
        city_s_time = int(2 * city_s_hour + city_s_minute//30) # K*0.5hour
        city_e_time = int(2 * city_e_hour + city_e_minute//30) + 1
        rect(screen, i, city_s_time,city_e_time)
        i += 1
        #print(i)
    color_temp += 32
    counter = color_temp // 256
    B = R = G = color_temp % 255
    if counter % 3 == 0:
        R = 0
    elif counter % 3 == 1:
        B = 192
        R = 48
    else:
        R = 192
        G = 48
    pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    screen.fill(bgc)
    pygame.display.flip()
    pygame.display.set_caption('City Time')
    e_w, e_h = screen_width / (city_num+2), screen_height / 22
    #pygame.draw.line(screen,color,(100,100),(500,400),width)
    draw(screen, screen_size, line, city)
    drawText(screen,time_day,e_w/2,e_h)
    pygame.display.update()
    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x,mouse_y == pygame.mouse.get_pos()
        if e_w<mouse_x<2*e_w and 2*e_h<mouse_y:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        check_events(screen, screen_size)

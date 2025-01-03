import os
from math import sqrt
class location():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z


# event1 = location(0, 500, 2700)
# event2 = location(0, 400, 4000)
# event3 = location(0, 800, 3500)
# station1 = location(450, 410, 2100)
# station2 = location(450, 410, 2200)
# station3 = location(450, 410, 2300)
# station4 = location(450, 410, 2400)
# station5 = location(450, 410, 2500)
event1=location(-49.79,482.87,2714.51)
event2=location(-223.75,436.91,2604.57)
event3=location(-67.33,409.27,2729.68)
station1=location(7.307,90.846,2120.657)
station2=location(7.699,91.244,2135.647)
station3=location(8.061,91.651,2150.637)
station4=location(8.396,92.060,2165.628)
station5=location(8.710,92.467,2180.619)
events = [event1, event2, event3]
stations=[station1,station2,station3,station4,station5]


for i in range(3):
    for j in range(5):
        model = 'HK'##速度模型
        npts  = 1024##采样点数
        dt    = 0.0005##时间采样间隔
        ed=sqrt((events[i].x-stations[j].x)**2+(events[i].y-stations[j].y)**2)/1000##震中距
        fk='fk.pl -M%s/%f -N%d/%f -R%f -S2 %f\n'%(model,  events[i].z/1000, npts, dt,stations[j].z/1000,ed)
        ##fk1='fk.pl -M%s/%f -N%d/%f -R%f -S0 %f\n'%(model,  events[i].z/1000, npts, dt,stations[j].z/1000,ed)
        print(fk)
        # print(fk1)
        os.system(fk)
        # os.system(fk1)

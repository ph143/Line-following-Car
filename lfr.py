import time
from machine import Pin
ls=Pin(2,Pin.IN)
rs=Pin(3,Pin.IN)
led=Pin(0,Pin.OUT)
m1=Pin(6,Pin.OUT)
m2=Pin(7,Pin.OUT)
m3=Pin(8,Pin.OUT)
m4=Pin(9,Pin.OUT)

while True:
    led.value(1)
    if(ls.value()==0 and rs.value()==0):
            m1.value(1)
            m2.value(0)
            m3.value(1)
            m4.value(0)
    led.value(1)
    elif(ls.value()==1 and rs.value()==1):
            m1.value(0)
            m2.value(0)
            m3.value(0)
            m4.value(0) 
    led.value(1)
    elif(ls.value()==1):
            m1.value(1)
            m2.value(0)
            m3.value(0)
            m4.value(1)
            time.sleep(0.1)
    led.value(1)
    elif(rs.value()==1):
            m1.value(0)
            m2.value(1)
            m3.value(1)
            m4.value(0)
            time.sleep(0.1)
    led.value(1)    
    
   
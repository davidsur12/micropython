from machine import Pin ,I2C , ADC , UART
from ssd1306 import SSD1306_I2C
import random
from time import sleep
import framebuf
import errno
import os
import utime

i2c=I2C(0 , sda=Pin(16) , scl=Pin(17) , freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

trigger = Pin(12, Pin.OUT)
echo = Pin(13, Pin.IN)

oled.text("hola", 64 , 30 , 1 )
oled.show()

def ultra():
    
    signaloff = 0
    signalon=0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ",distance,"cm")
    oled.fill(0)
    oled.text(str(int(distance)) +  "    cm", 30 , 30 , 1 )
    oled.show()

   

while True:
   ultra()
   utime.sleep(1)
   
oled.text("hola", 64 , 30 , 1 )
oled.show()
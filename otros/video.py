from machine import Pin ,I2C , ADC , UART
from ssd1306 import SSD1306_I2C
import random
from time import sleep
import framebuf
import errno
import os


i2c = I2C(1 , sda=Pin(18), scl=Pin(19)  , freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

def str_list_to_int_list(str_list ):
    n = 0
    while n < len(str_list):
        #str_list[n] = bytes(str_list[n] , 'utf-8')
        str_list[n] = int(str_list[n] )
        n += 1
    return(str_list)
print(os.listdir())
#fp = open("ima2.txt" , "r")

    
        
  
    


from machine import Pin ,I2C , ADC
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import random
 
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
i2c=I2C(1,sda=Pin(18), scl=Pin(19), freq=400000 )

utime.sleep_ms(100)
oled = SSD1306_I2C(128, 64, i2c)
def movimiento(j):
      
    for i in range(64 , 40,-1):
        oled.vline (j, i, 10, 1)
        
        oled.show();
        utime.sleep(0)
        oled.fill(0)
    cont=0;    
    for c in range(0,30):
        cont=cont+1
        oled.pixel(j+cont , 40 , 1 )#dercha
        oled.pixel(j-cont , 40 , 1)#izquierda
        oled.pixel(j , 40+cont , 1) #arriba
        oled.pixel(j , 40-cont , 1)#abajo
        oled.pixel(j+cont , 40+cont ,1)
        oled.pixel(j+cont , 40-cont ,1)
        oled.pixel(j-cont , 40+cont ,1)
        oled.pixel(j-cont , 40-cont ,1)
        oled.show();
        utime.sleep(0)
        oled.fill(0)
   
    
    #oled.line(0,10,10,60,1);#x,y
    #oled.pixel(2,2,1)
    
    
   
  

while True:
    num = random.randint(1, 128)
    movimiento(num)   


    
    
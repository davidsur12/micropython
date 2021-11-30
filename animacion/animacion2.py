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
def movimiento():
    
    cont=1
    cont2=1
    espacio=1
    fila=10
    columna=64
    
    for i in range(1 , 17):
        
        for j in range(1 , i ):
            
            oled.text(str(cont), columna, fila)
            oled.show()
            columna=columna+(espacio)
            espacio=espacio+2
            cont=cont+1
        cont2=cont+1
        columna=64-(cont2*4)
        fila=fila+(9)
         
   
     
     
      
  
    
   
  

movimiento()
    
from machine import Pin ,I2C , ADC , UART
from ssd1306 import SSD1306_I2C
import random
from time import sleep
import framebuf

i2c = I2C(1 , sda=Pin(18), scl=Pin(19)  , freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
hc06=UART(1 , 9600)
frame = [0];
cont=0;
f=[]
f2=[]
f3=[]
while True:
    if(cont >= 1088):
    
        print("_______________________________________________________________")    
        cont=0
        print("tipo f2 = " , f2[0])
        print("tipo f2 = "  , type(frame[0]))
       
        print(type(frame))
        print(type(f2[0]))
        print("len de f2 " , len(f2))
       
       
        oled.fill(0)
        #fram=bytearray(f2)
      
        
        fram=bytearray(f2)
        fb=framebuf.FrameBuffer(fram , 128 , 68  , framebuf.MONO_HLSB);
        oled.blit(fb , 0 , 0)#columna , fila
        oled.show()
        sleep(2)
        f2=[]
       
      
       
        
        
        
        
    if hc06.any()>0:
        date=hc06.readline()
        """
        print("typo de datos de date = " , type(date))
        print("ancho date = " ,  len(date))
        #print(date)
        print("tipo  de frame" , type(frame[0]))
        l=[255]
        print("array array l = " , type(l[0]))
        print("se puede acceder como un lista de array date " , date[0])
        """
        #frame.append(date)
        for i in range(0 ,len(date)):
            f2.append(int(float(date[i])))
            #print(f2[i])
        cont=cont + len(date)
        """
        print("typo de datos f2 = " , type(f2[i]))
        
        oled.fill(0)
        oled.text(date , 0 , 0 , 1)
        oled.show()
        print("___________________________________________________________________________________")
        """
    
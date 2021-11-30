from machine import Pin ,I2C , ADC 
from ssd1306 import SSD1306_I2C
import framebuf
import utime

 
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)
i2c=I2C(1,sda=Pin(18), scl=Pin(19), freq=400000 )

utime.sleep_ms(100)
oled = SSD1306_I2C(128, 64, i2c)

btn1 = Pin(21, Pin.IN, Pin.PULL_DOWN)
btn2 = Pin(20, Pin.IN, Pin.PULL_DOWN)
ledstxt= ['LED 1', 'LED 2' , 'LED 3']
estado=['OFF', 'OFF' , 'OFF']
estadoLeds=[False , False , False]
#led1=Pin(13, Pin.OUT)
leds=[Pin(13, Pin.OUT) , Pin(14, Pin.OUT) , Pin(15, Pin.OUT) ]
buzzer=Pin(26, Pin.OUT) 
#led1.value(0)
def menu(lista , pos , ok):
    oled.fill(0)
    oled.show()
    fila=20;
    
    for i in range(0 , len(ledstxt)):
        if(pos==i):
            
            oled.fill_rect(0, fila-2, 128, 13, 1) #pocicion inicial ancho largo
            oled.text(ledstxt[i],10 , fila,0 )
        else:
            oled.text(ledstxt[i],10 , fila,1 )
            
               
        
        oled.show()
        #utime.sleep(2)
        fila=fila+15
    
    cambioEstado(cont , estadoLeds , ok)
 
def cambioEstado(pos , estados , ok):
      #oled.fill(0)
      #oled.show()
      fila=20;
      
      for i in range(0 , len(ledstxt)):
          
          if(pos==i):
              
              #oled.fill_rect(0, fila-2, 128, 13, 1) #pocicion inicial ancho largo
              if  ok==True:
                  if estados[i]:
                      
                      estados[i]=False
                      estado[i]="OFF"
                      leds[i].value(0)
                      buzzer.value(1)
                      utime.sleep(0.1)
                      buzzer.value(0)
                  else:
                      
                      estados[i]=True
                      estado[i]="ON"
                      leds[i].value(1)
                      buzzer.value(1)
                      utime.sleep(0.1)
                      buzzer.value(0)
                  
                  
              oled.text(estado[i],100 , fila,0 )
              
              
              
          else:
              
              oled.text(estado[i],100 , fila,1 )
            
               
        
          oled.show()
          #utime.sleep(2)
          fila=fila+15
    
    
    
cont=0
menu(ledstxt,cont , False)
cambioEstado(cont , estadoLeds , False)
while True:
    
    if(btn2.value()):
        
        #cambioEstado(cont , estadoLeds ,True)
        menu(ledstxt,cont,True)
    if btn1.value():#itera
        cont=cont+1
        if (cont==3):
            cont=0
        utime.sleep(0.3)    
        
        
        menu(ledstxt,cont,False)
        utime.sleep(0.3)
        
        """
        oled.text("encedido",10 , 10 , 1)
        oled.show()
        utime.sleep(0.5)
        oled.fill(0)
        oled.show()
        """
	    
	    


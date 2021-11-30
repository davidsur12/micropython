from machine import Pin ,I2C , ADC
from ssd1306 import SSD1306_I2C
import random
from time import sleep
import framebuf

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
pot=ADC(26)
factor = 3.3 / (65535)

bird=[3,192,0,3,192,0,3,96,0,2,231,0,27,111,8,27,223,12,1,223,12,24,221,12,26,31,12,3,223,12,3,216,8,1,230,8,0,6,0,0,6,0,0,0,0]
flapy=bytearray(bird)

gameover=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,255,129,255,240,0,0,0,31,255,129,255,240,0,0,0,120,1,231,128,60,0,0,0,120,1,231,128,60,0,0,0,96,0,102,0,12,0,0,0,96,0,102,0,12,0,0,0,96,0,102,4,12,0,0,0,96,0,102,4,12,0,0,0,120,1,231,132,60,0,0,0,120,1,231,132,60,0,0,0,31,255,129,252,48,0,0,0,31,255,129,252,49,128,0,0,0,0,0,0,1,128,0,0,0,0,0,0,1,128,0,0,7,255,231,255,193,128,0,0,31,255,231,255,241,255,255,12,126,0,0,24,253,255,255,14,120,0,0,24,61,128,0,3,96,0,0,24,13,128,0,3,96,0,0,24,13,128,0,1,96,0,0,24,13,128,6,1,96,0,0,24,13,128,6,1,120,0,0,24,61,128,6,1,126,0,0,24,253,128,6,1,31,255,231,255,241,128,6,1,0,0,0,0,1,135,255,9,0,0,0,0,1,128,6,1,127,255,231,255,253,128,6,1,127,255,231,255,253,128,6,1,96,96,96,0,13,128,6,1,96,96,96,0,125,128,6,1,96,96,96,7,249,128,0,1,96,96,96,7,129,128,0,3,96,96,96,7,193,128,0,3,96,96,96,3,253,255,255,14,96,96,96,0,61,255,255,12,96,96,103,255,253,128,0,0,96,0,103,255,253,128,0,0,0,0,0,0,1,128,0,0,0,0,0,0,1,128,0,0,127,255,231,255,252,0,0,0,127,255,231,255,252,0,0,0,1,192,102,4,12,0,0,0,1,192,102,4,12,0,0,0,3,192,102,4,12,0,0,0,7,192,102,4,12,0,0,0,14,192,102,4,12,0,0,0,28,192,102,4,12,0,0,0,24,241,230,4,12,0,0,0,48,241,230,4,12,0,0,0,112,63,134,0,12,0,0,0,96,63,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
over=bytearray(gameover)
button = Pin(14 , Pin.IN , Pin.PULL_UP)
led = Pin(25, Pin.OUT)
columna=50

def obstaculo(posx , posy  , posColumna ):
    oled.fill(0)
    #setPosBird(getPosBird() - 1)
    posColumna=posColumna - 2
    oled.fill_rect( posx,  posy,  128-posx ,  10 ,  1)#obstaculo ariba
    oled.fill_rect( 0,  posy ,  posx-30 ,  10 ,  1)#obstaculo abajo
    fb=framebuf.FrameBuffer(flapy , 20 , 15  , framebuf.MONO_HLSB);
    
   
    pos=int(leer_pot())
    #oled.text(str(pos) , 0 , 0 , 1)
    oled.blit(fb ,  posColumna , 16)#columna , fila
    oled.show()
    
    if(button.value()==0):
        #led.on()
        posColumnap = posColumna + 5
        if(posColumnap < 110):
            posColumna = posColumna + 5
            """
    if(posy>16 and pos<31):
        if(posColumna < posx-30):
            #oled.fill(0)
            #oled.text("perdist" , 0 ,0 ,1)
            #oled.show()
            #sleep(2)
            posColumna=200
            
        """
        
         
        
       
    #oled.text("posColumna = " + str(posColumna) , 0 , 0 ,1)
    #oled.text("posx = " + str(posx) , 0 , 9 , 1 )
    #oled.text("posy = " + str(posy) , 0 , 16 , 1)
    #oled.show()
    
    return posColumna    
        
           
    
def leer_pot():
    potentiometer = machine.ADC(26)
    #conversion_factor = 3.3 / (65535)
    #voltage = potentiometer.read_u16() * conversion_factor
    voltage = potentiometer.read_u16()
    porce=int((voltage*100)/65535)
    
    print(porce)
    return porce
    
    
    
def main():
    #16 filas son amarillas
    columnaa=50
    posx=128
    y=random.randrange(1 , 80 , 1 )
    oled.fill_rect(0 , 0 , 10 , 16 , 1)#columna , fila , ancho , largo
    oled.show()
    while False :
        oled.fill(0)
        posx=posx-1
        posxx="pos + 10 = " + str(posx+10)
        yyy="pos = " + str(y)
        oled.fill_rect(posx , 0 , 10, y, 1)   # Dibuja un rectángulo relleno iluminado. Origen (5, 3)y anchura x altura 14x12 píxels                    # Invierte lo que se va a mostrar
        #oled.text( yyy, 30, 50 , 1)
        oled.text( posxx , 0, 50 , 1)
        oled.show()
        sleep(0.2)
    posy=64
    obt1=[100 , posy , 30 , 10]
    cont=0
    sensor = ADC(26)
    while True:
        #y=random.randrange(50 , 120 , 1 )
        #obst(y)
        posx=random.randrange(50 , 120 , 1 )
        for posy in range(64 , 1 , -1 ):
            
            columnaa=obstaculo(posx , posy , columnaa)
            sleep(0.1)
            
            if(columna == 200):
                oled.fill(0)
                oled.show()
                oled.text("perdiste " , 0 , 0 , 1)
                oled.show()
                columnaa=50
                sleep(3)
                break
            if(posy >16 and posy<=39):
                if(columnaa < posx-30 or  columnaa > posx):
                    oled.fill(0)
                    oled.show()
                    #oled.text("perdiste " , 0 , 0 , 1)
                    fb=framebuf.FrameBuffer(over , 60 , 60  , framebuf.MONO_HLSB);
                    oled.blit(fb ,  40 , 0)#columna , fila
                    oled.show()
                    columnaa=50
                    sleep(3)
                    break
                    
                    
            #si choko con los bordes
            if(columnaa < 0):
                oled.fill(0)
                oled.show()
                #oled.text("perdiste " , 0 , 0 , 1)
                fb=framebuf.FrameBuffer(over , 60 , 60  , framebuf.MONO_HLSB);
                oled.blit(fb ,  40 , 0)#columna , fila
                oled.show()
                columnaa=50
                sleep(3)
                break
            
            #leer_pot()
            
                
          
            #sleep(1);
                      
if __name__== '__main__':
    main();     
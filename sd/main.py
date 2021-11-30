from machine import Pin, SPI
import sdcard
import os
 
spi=SPI(1,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
sd=sdcard.SDCard(spi,Pin(15))
vfs=os.VfsFat(sd)
 
os.mount(sd,'/sd')
print(os.listdir('/sd'))

"""
from machine import Pin, I2C ,  SPI
from ssd1306 import SSD1306_I2C
import sdcard
import os



#i2c=I2C(1,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, I2C(1))
oled.text("Tom's Hardware", 0, 0)
oled.show()
"""
"""
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
sda=machine.Pin(19)
scl=machine.Pin(20)
#i2c=machine.I2C(0,sda=sda, scl=scl , freq=400000)
#oled = SSD1306_I2C(128, 64, I2C)#argumentos ancho , alto , comunicacion
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.text("Tom's Hardware", 0, 0)
oled.show()
"""
"""
import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
while True:
    led_onboard.value(1)
    utime.sleep(0.5)
    led_onboard.value(0)
    utime.sleep(0.5)
"""
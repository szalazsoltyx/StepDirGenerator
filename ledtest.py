from machine import Pin, PWM
import time

led_core = Pin(2, Pin.OUT) #core
#led_stepp = machine.Pin(15, machine.Pin.OUT) #d8
led_stepp = PWM(Pin(15)) #d8
led_dir = machine.Pin(16, machine.Pin.OUT)# d0 

led_stepp.deinit()
led_core(1)
'''
for i in range(10):
    led_stepp(0)
    time.sleep(0.5)
    led_stepp(1)
    time.sleep(0.5)
'''

led_stepp.duty(511)
led_stepp.freq(2000)
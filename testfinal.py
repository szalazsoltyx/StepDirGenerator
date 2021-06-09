from machine import Pin, I2C, PWM
import ssd1306
import time
from rotary_irq_esp import RotaryIRQ

# ESP8266 Pin assignment
button = Pin(14, Pin.IN, Pin.PULL_UP)
i2c = I2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

led_core = Pin(2, Pin.OUT) #core
#led_stepp = machine.Pin(15, machine.Pin.OUT) #d8
#led_stepp = PWM(Pin(15)) #d8
led_dir = machine.Pin(16, machine.Pin.OUT)# d0 

led_core(1) #Alapli led kikapcs

def menu(status):
    oled.fill(0)
    if status == 0:
        oled.text('> Step', 0, 0)
        oled.text('  Frequency',0 , 10)
        oled.text('  Cycle', 0, 20 )
        oled.show()
    elif status == 1:
        oled.text('  Step', 0, 0)
        oled.text('> Frequency',0 , 10)
        oled.text('  Cycle', 0, 20 )
        oled.show()
    elif status == 2:
        oled.text('  Frequency',0 , 0)
        oled.text('> Cycle', 0, 10 )
        oled.text('  Start', 0, 20 )

        oled.show()
    elif status == 3:
        oled.text('  Frequency',0 , 0)
        oled.text('  Cycle', 0, 10 )
        oled.text('> Start', 0,20)
        oled.show()        

def ertek(current, active_menu):
    oled.fill(0)
    oled.text(active_menu, 0, 0)
    oled.text(str(current), 0, 10)
    oled.show()

def mine(min=0, max=10, status=False):
    r = RotaryIRQ(pin_num_clk=12,
                pin_num_dt=13,
                min_val=min,
                max_val=max,
                reverse=False,
                range_mode=RotaryIRQ.RANGE_WRAP)

    val_old = -1 #atveres hogy frissujon az oldal

    while True:
        val_new = r.value()
        first = button.value()
        time.sleep(0.01)
        second = button.value()

        if val_old != val_new:
            val_old = val_new
            if status == False:
                menu(val_new)
            else: 
                ertek(val_new, status)

        elif first and not second:
            return val_new
        elif not first and second:
            pass #print('Button released!')

def vezerles(Step=1, Freqency=0.5, Cycle=1):
    '''
    0.0019 sec a DRV8825 vezerlö szerint minimumertek 
    '''
    led_stepp = machine.Pin(15, machine.Pin.OUT) #d8
    for n in range(Cycle):
        for i in range(Step):
            led_stepp(0)
            time.sleep(Freqency)
            led_stepp(1)
            time.sleep(Freqency)


def vezerles_sima(Step=1, Freqency=0.5, Cycle=1):
    led_stepp = machine.Pin(15, machine.Pin.OUT) #d8
    for n in range(Cycle):
        for i in range(Step):
            led_stepp(0)
            time.sleep(Freqency)
            led_stepp(1)
            time.sleep(Freqency)

def vezerles_pwm(Step=1, Freqency=10, Cycle=1):
    led_stepp = PWM(Pin(15))
    for i in range(Cycle):
        led_stepp.deinit()
        led_stepp.duty(511) #50% os kitöltöttség
        led_stepp.freq(Freqency) # max 1000?
        time.sleep(Step)


menuelems = ['Step :', 'Frequency :', 'Cycle :', 'Start' ]

while True:
    menu_selected = mine(0, 3, False)
    active_menu=(menuelems[menu_selected])
    
    if menu_selected == 0:
        menu0 =  mine(0, 5, active_menu) #Step
    elif menu_selected == 1:
        menu1 =  mine(0, 100, active_menu) #Frequency
    elif menu_selected == 2:
        menu2 =  mine(0, 5, active_menu) #Cycle
    elif menu_selected == 3:
        #print('vegae a dalnak',menu0 ,menu1, menu2 )
        kiirando = str(menu0)+','+str(menu1)+','+str(menu2)
        mine(0, 1, kiirando)
        vezerles_pwm(menu0, menu1, menu2)
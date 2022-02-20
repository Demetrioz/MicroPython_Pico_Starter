import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.In, machine.Pin.PULL_DOWN)

while True:
    # led_onboard.value(1)
    # utime.sleep(1)
    # led_onboard.value(0)
    
    # led_onboard.toggle()
    # utime.sleep(1)
    
    if button.value() == 1:
       led_onboard.toggle()
       utime.sleep(2)
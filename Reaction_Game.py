import machine
import utime
import urandom

pressed = False
fastest_button = None
led = machine.Pin(15, machine.Pin.OUT)
button_1 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_2 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    global pressed
    global fastest_button
    if not pressed:
        pressed = True
        #print(pin)
        fastest_button = pin
        timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
        print(f"Your reaction time was {timer_reaction} milliseconds")

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)

timer_start = utime.ticks_ms()
button_1.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)
button_2.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while fastest_button is None:
    utime.sleep(1)

if fastest_button is button_1:
    print("Player 1 wins!")
elif fastest_button is button_2:
    print("Player 2 wins!")
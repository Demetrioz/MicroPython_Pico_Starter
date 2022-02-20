import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(12, machine.Pin.OUT)

def handle_pir(pin):
    # Prevent a being triggered due to jitter from the signal (debouncing)
    utime.sleep_ms(100)
    if pin.value():
        #if pin is sensor_pir:
        #    print("Alarm in room 1")
        #elif pin is sensor_pir_2:
        #    print("Alarm is room 2")
        print("ALARM! Motion detected!")
        for i in range(50):
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
        
sensor_pir.irq(trigger = machine.Pin.IRQ_RISING, handler = handle_pir)

while True:
    led.toggle()
    utime.sleep(5)
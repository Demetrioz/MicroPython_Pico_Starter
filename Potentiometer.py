import machine
import utime

potentiometer = machine.ADC(26)
internal_temp = machine.ADC(4)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

conversion_factor = 3.3 / (65535)

while True:
    voltage = potentiometer.read_u16() * conversion_factor
    temp_reading = internal_temp.read_u16() * conversion_factor
    temp_c = 27 - (temp_reading - 0.706)/0.001721
    # print(voltage)
    # print(temp_c)
    # utime.sleep(2)
    # Read the uint16 value from the potentiometer, and set that as the
    # duty cycle for the led - controlling the brightness via the
    # potentiometer
    led.duty_u16(potentiometer.read_u16())
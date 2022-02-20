import machine
import utime

sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
conversion_factor = 3.3 / (65535)

with open("temps.txt", "a") as file:
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706) / 0.001721
        file.write(str(temperature) + "\n")
        utime.sleep(5)
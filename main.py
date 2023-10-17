import odroid_wiringpi as wpi
import time
import os

#connect to odroid
# connecting to a pwm pin (GPIO18)
p = 1

wpi.wiringPiSetup()
wpi.pinMode(p, wpi.PWM_OUTPUT)

for _ in range(1):
    for duty_cycle in range(50, 250, 5):  # Adjust values to match your servo's specifications
        wpi.pwmWrite(p, duty_cycle)
        time.sleep(0.02)
    time.sleep(1)
    for duty_cycle in range(250, 50, -5):  # Adjust values to match your servo's specifications
        wpi.pwmWrite(p, duty_cycle)
        time.sleep(0.02)
    time.sleep(1)

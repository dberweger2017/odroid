import odroid_wiringpi as wpi
import time

wpi.wiringPiSetup()
wpi.pinMode(11, wpi.PWM_OUTPUT)

while True:
    for duty_cycle in range(50, 250, 5):  # Adjust values to match your servo's specifications
        wpi.pwmWrite(11, duty_cycle)
        time.sleep(0.02)
    time.sleep(1)
    for duty_cycle in range(250, 50, -5):  # Adjust values to match your servo's specifications
        wpi.pwmWrite(11, duty_cycle)
        time.sleep(0.02)
    time.sleep(1)

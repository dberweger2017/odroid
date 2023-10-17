import odroid_wiringpi as wpi
import time

for i in range(1,40):

    print(f"Trying pin {i}")

    wpi.wiringPiSetup()
    wpi.pinMode(i, wpi.PWM_OUTPUT)

    for _ in range(5):
        for duty_cycle in range(50, 250, 5):  # Adjust values to match your servo's specifications
            wpi.pwmWrite(i, duty_cycle)
            time.sleep(0.02)
        time.sleep(1)
        for duty_cycle in range(250, 50, -5):  # Adjust values to match your servo's specifications
            wpi.pwmWrite(i, duty_cycle)
            time.sleep(0.02)
        time.sleep(1)

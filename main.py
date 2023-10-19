import odroid_wiringpi as wpi

# Initialize WiringPi
wpi.wiringPiSetup()

# Set the pin number (assuming pin 33, you might need to adjust this)
pin = 1

# Create a software-controlled PWM
wpi.softPwmCreate(pin, 0, 200)

# Sweep the servo from 0 to 180 degrees
for angle in range(0, 181):
    duty_cycle = int((angle / 180.0) * 200)
    wpi.softPwmWrite(pin, duty_cycle)
    wpi.delay(10)  # Adjust delay to control speed of sweep

# Clean up
wpi.pinMode(pin, wpi.INPUT)

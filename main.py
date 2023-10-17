import wiringpi
import time

# Use WiringPi numbering
wiringpi.wiringPiSetup()

pinNumber = 1  # Change this to your GPIO pin number

# Set the pin to be in PWM output mode
wiringpi.pinMode(pinNumber, wiringpi.GPIO.PWM_OUTPUT)

# Set PWM mode to milliseconds type
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# Set the base frequency for PWM
baseFrequency = 1920  # For 50Hz, change this if you need a different frequency
wiringpi.pwmSetClock(baseFrequency)

# Set the range for PWM
rangeValue = 2000  # This is typical for servos
wiringpi.pwmSetRange(rangeValue)

# Helper function to set the servo position
def set_servo_position(pin, position):
    # Convert the servo position (0-180) to PWM value
    pwm_value = int(((position / 180.0) * (240 - 50)) + 50)
    wiringpi.pwmWrite(pin, pwm_value)

# Example: Move servo from 0 to 180 degrees, then back to 0
set_servo_position(pinNumber, 0)
time.sleep(1)
set_servo_position(pinNumber, 180)
time.sleep(1)
set_servo_position(pinNumber, 0)


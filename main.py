import mraa
import time

# Initialize PWM on PWM pin (Check your board's pinout for the right pin number)
pwm_pin = 3  # Change this to your actual PWM pin number
servo = mraa.Pwm(pwm_pin)

# Enable the PWM pin
servo.enable(True)

# Set the PWM period in microseconds (this example uses 50Hz: 1/50 = 0.02s or 20000us)
servo.period_us(20000)

# Helper function to set the servo position
def set_servo_position(servo, position):
    # Convert the servo position (0-180) to duty cycle (usually between 0.03 and 0.12)
    duty_cycle = 0.03 + ((position / 180.0) * (0.12 - 0.03))
    servo.write(duty_cycle)

# Example: Move servo from 0 to 180 degrees, then back to 0
set_servo_position(servo, 0)
time.sleep(1)
set_servo_position(servo, 180)
time.sleep(1)
set_servo_position(servo, 0)

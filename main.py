import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
SERVO_PIN = 3  # Use PWM_D pin
GPIO.setup(SERVO_PIN, GPIO.OUT)

# Set the PWM frequency
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz frequency
pwm.start(7.5)  # Middle position

try:
    while True:
        # Rotate servo to 0 degrees
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        
        # Rotate servo to 90 degrees (middle)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        
        # Rotate servo to 180 degrees
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

import streamlit as st
import odroid_wiringpi as wpi

# Initialize WiringPi
wpi.wiringPiSetup()

# Set the pin number (assuming pin 33, you might need to adjust this)
pin = 1

# Create a software-controlled PWM
wpi.softPwmCreate(pin, 0, 200)

st.title("Servo Controller")

min_1 = 0
max_1 = 30

# Streamlit slider
angle_to_move = st.slider("Select angle to move to:", min_value=min_1, max_value=max_1, step=1)

try:
    # Move to specific angle
    duty_cycle = int((angle_to_move / 180.0) * 200)
    wpi.softPwmWrite(pin, duty_cycle)
    st.write(f"Moved to angle: {angle_to_move}")

except Exception as e:
    st.write(f"An error occurred: {e}")

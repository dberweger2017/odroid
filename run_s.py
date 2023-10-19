import streamlit as st
import odroid_wiringpi as wpi
import numpy as np

# Initialize WiringPi
wpi.wiringPiSetup()

# Set the pin number (assuming pin 33, you might need to adjust this)
pin = 1

# Create a software-controlled PWM
wpi.softPwmCreate(pin, 0, 200)

st.title("Servo Controller")

min_1 = 5
max_1 = 21

# Streamlit slider
angle_to_move = st.slider("Select angle to move to:", min_value=min_1, max_value=max_1, step=1)

try:
    # Move to specific angle
    duty_cycle = int((angle_to_move / 180.0) * 200)
    wpi.softPwmWrite(pin, duty_cycle)
    st.write(f"Moved to angle: {angle_to_move}")

except Exception as e:
    st.write(f"An error occurred: {e}")

st.progress(0)

run = st.button("Run")
if run:
    for i in range(100):
        st.progress(i)
        rand = np.random.randint(min_1, max_1)
        duty_cycle = int((rand / 180.0) * 200)
        wpi.softPwmWrite(pin, duty_cycle)
        st.write(f"Moved to angle: {rand}")
        wpi.delay(200)
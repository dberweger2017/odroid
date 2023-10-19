import streamlit as st
import numpy as np
import odroid_wiringpi as wpi

st.title("Servo control")

angle = st.slider("Angle", 0, 180, 90)

# Initialize WiringPi
wpi.wiringPiSetup()

# Initialize WiringPi
wpi.wiringPiSetup()

pin = 1

wpi.softPwmCreate(pin, 0, 200)
duty_cycle = int((angle / 180.0) * 200)
wpi.pinMode(pin, wpi.INPUT)
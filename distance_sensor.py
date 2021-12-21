#!/usr/bin/python

# https://pimylifeup.com/raspberry-pi-distance-sensor/
# https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

# Libraries
import RPi.GPIO as GPIO
import time

# Set GPIO Mode
GPIO.setmode(GPIO.BOARD)

# Set GPIO Pins
PIN_TRIGGER = 7
PIN_ECHO = 11

# Set GPIO direction(IN / OUT)
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

def distance():

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    time.sleep(2)

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    current_time = time.time()
    pulse_start_time, pulse_end_time = current_time, current_time
    

    while GPIO.input(PIN_ECHO) == 0:
        pulse_start_time = time.time()

    while GPIO.input(PIN_ECHO) == 1:
        pulse_end_time = time.time()
    
    pulse_duration = pulse_end_time - pulse_start_time

    distance = round(pulse_duration * 34300 * 0.5, 2)

    return distance
    
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Distance: " + str(dist) + " cm")

    # Reset by pressing Ctrl + C
    except KeyboardInterrupt:
        print("")
        print("Measurement stopped by User")
        GPIO.cleanup()

import time
import paho.mqtt.client as mqtt
import json
from grove.adc import ADC
from os import system, name

print("Soil Moisture Sensor")

adc = ADC()

mqtt_server = '192.168.1.102'               # Ignition server (Raspberry Pi 4)

id = 'pi-zero-2w'

client_name = id + 'soil_moisture_sensor_client'
client_telemetry = id + '/telemetry/'

mqtt_client = mqtt.Client(client_name)

mqtt_client.connect(mqtt_server)

mqtt_client.loop_start()
print("MQTT Connected")

# https://www.geeksforgeeks.org/clear-screen-python/
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux (here, os.name is 'posix')
    else:
        _ = system('clear')



while True:
    soil_moisture = adc.read(0)
    print("Soil moisture: ", soil_moisture)

    time.sleep(5)

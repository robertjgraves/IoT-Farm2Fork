import time
import paho.mqtt.client as mqtt
import json
from seeed_dht import DHT
from os import system, name

print("Temperature Sensor")

sensor = DHT("11", 5)

mqtt_server = '192.168.1.102'               # Ignition server (Raspberry Pi 4)
#mqtt_server = 'test.mosquitto.org'         # public mosquitto server
#mqtt_client = '192.168.1.107'              # local mosquitto server

id = 'pi-zero-2w'

client_name = id + 'temperature_sensor_client'
client_telementry = id + '/telemetry/'

mqtt_client = mqtt.Client(client_name)

mqtt_client.connect(mqtt_server)

mqtt_client.loop_start()
print("MQTT Connected")

def CtoF(celsius):
    return celsius * (9.0 / 5.0) + 32.0

# https://www.geeksforgeeks.org/clear-screen-python/
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
    
    # for mac and linux (here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == '__main__':
    try:
        while True:
            clear()
            print("Temperature Sensor")
            
            hum, tempC = sensor.read()
            tempF = CtoF(tempC)

            data = {}
            data["tempC"] = tempC
            data["humidity"] = hum
            data["tempF"] = tempF
            data["time"] = time.time()

            print(f'Temperature {tempC:.1f}°C / {tempF:.1f}°F \tHumidity {hum}% \tTime {data["time"]}')

            telementry = json.dumps(data)
            
            mqtt_client.publish(client_telementry, telementry)
            
            time.sleep(10)
    
    except KeyboardInterrupt:
        print("")
        print("Stopped by user")


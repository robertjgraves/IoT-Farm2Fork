import time
import paho.mqtt.client as mqtt
import json
from seeed_dht import DHT

print("Temperature Sensor")

sensor = DHT("11", 5)

id = '264d5b81-aac4-4d74-aa92-9539914e2cbd'

client_name = id + 'temperature_sensor_client'
client_telementry = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
#mqtt_client.connect('test.mosquitto.org')
mqtt_client.connect('192.168.1.107')

mqtt_client.loop_start()
print("MQTT Connected")

def CtoF(celsius):
    return celsius * (9.0 / 5.0) + 32.0

if __name__ == '__main__':
    try:
        while True:
            hum, temp = sensor.read()
            tempF = CtoF(temp)
            telementry = json.dumps({'temperature C' : temp, 'humidity' : hum, 'temperature F' : tempF})
            mqtt_client.publish(client_telementry, telementry)
            
            print(f'Temperature {temp:.1f}°C / {tempF:.1f}°F \tHumidity {hum}%')
            time.sleep(2)
    
    except KeyboardInterrupt:
        print("")
        print("Stopped by user")


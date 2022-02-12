import json
import time
import paho.mqtt.client as mqtt

mqtt_server = '192.168.1.102'               # Ignition server (Raspberry Pi 4)

id = 'pi-zero-2w'

client_telemetry_top = id + '/telemetry'
client_name = id + 'soil_moisture_sensor_server'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect(mqtt_server)

mqtt_client.loop_start()



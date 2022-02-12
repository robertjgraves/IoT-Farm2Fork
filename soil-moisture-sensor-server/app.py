import json
import time
import paho.mqtt.client as mqtt

mqtt_server = '192.168.1.102'               # Ignition server (Raspberry Pi 4)

id = 'pi-zero-2w'

client_telemetry_topic = id + '/telemetry/'
client_name = id + 'soil_moisture_sensor_server'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect(mqtt_server)

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

if __name__ == '__main__':
    try:
        while True:
            time.sleep(2)

    except KeyboardInterrupt:
        print("")
        print("Stopped by user")


import time
import paho.mqtt.client as mqtt
import json
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_led import GroveLed

light_sensor = GroveLightSensor(0)
led = GroveLed(5)

# https://www.guidgen.com
id = '264d5b81-aac4-4d74-aa92-9539914e2cbd'

client_name = id + 'nightlight_client'
client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')
#mqtt_client.connect('192.168.1.107')

mqtt_client.loop_start()

print("MQTT Connected")

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['led_on']:
        led.on()
    else:
        led.off()

mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

if __name__ == '__main__':
    try:
        while True:
            light = light_sensor.light
            telemetry = json.dumps({'light': light})

            print("Sending telemetry ", telemetry)

            mqtt_client.publish(client_telemetry_topic, telemetry)

            time.sleep(2)
    
    except KeyboardInterrupt:
        print("")
        print("Stopped by user")
        
    finally:
        led.off()
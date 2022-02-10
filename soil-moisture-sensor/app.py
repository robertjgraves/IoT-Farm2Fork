import time
import paho.mqtt.client as mqtt
import json
from grove.adc import ADC
from os import system, name
from grove.grove_relay import GroveRelay


adc = ADC()
relay = GroveRelay(16)

mqtt_server = '192.168.1.102'               # Ignition server (Raspberry Pi 4)
soil_sensor_analog_port = 0

id = 'pi-zero-2w'

client_name = id + 'soil_moisture_sensor_client'
client_telemetry = id + '/telemetry/'

mqtt_client = mqtt.Client(client_name)

mqtt_client.connect(mqtt_server)

mqtt_client.loop_start()
print("MQTT Connected")

def test_relay():
    print("")
    print("Testing relay")
    print("Relay on")
    relay.on()
    
    time.sleep(.5)

    print("Relay off")
    print("")
    relay.off()

def relay_control(soil_moisture):
    if soil_moisture > 450:
        print("Soil moisture is too low, turning relay on.")
        relay.on()
    
    else:
        print("Soil Moisture is okay, turning relay off.")
        relay.off()

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
            
            print("Soil Moisture Sensor")
            soil_moisture = adc.read(soil_sensor_analog_port)
            
            relay_control(soil_moisture)

            data = {}
            data["soil moisture"] = soil_moisture

            telemetry = json.dumps(data)

            mqtt_client.publish(client_telemetry, telemetry)

            print("Soil moisture: ", soil_moisture)

            time.sleep(5)

    except KeyboardInterrupt:
        print("")
        print("Stopped by user")
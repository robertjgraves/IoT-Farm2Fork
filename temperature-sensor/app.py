import time
from seeed_dht import DHT

print("Temperature Sensor")

sensor = DHT("11", 5)

def CtoF(celsius):
    return celsius * (9.0 / 5.0) + 32.0

if __name__ == '__main__':
    try:
        while True:
            hum, temp = sensor.read()
            tempF = CtoF(temp)
            print(f'Temperature {temp:.1f}°C / {tempF:.1f}°F \tHumidity {hum}%')
            time.sleep(2)
    
    except KeyboardInterrupt:
        print("")
        print("Stopped by user")


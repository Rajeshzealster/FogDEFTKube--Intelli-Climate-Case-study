import sys
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
import paho.mqtt.client as mqtt

if len(sys.argv) == 2:
    broker_url=sys.argv[1]
    user=""
elif len(sys.argv)==3:
    broker_url=sys.argv[2]
    user=sys.argv[2]
else:
    # If the BROKER_ADDRESS argument is not provided, display information on how to execute the program
    print("Usage: python your_script.py [AUTHOR] BROKER_ADDRESS:PORT")
    print("Example: python your_script.py 192.168.0.204:30001")
    sys.exit(1)  # Exit with a non-zero status code to indicate an error

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)


broker_address, broker_port=broker_url.split(":")
topic = "sensor/"+user+"/data" if user else "sensor/data"

# MQTT client initialization
client = mqtt.Client()
client.connect(broker_address, int(broker_port))

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

            # publish sensor data to MQTT broker
            payload = json.dumps({"temperature": result.temperature, "humidity": result.humidity})
            client.publish(topic, payload)
            print("Published to MQTT broker from "+user)

        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

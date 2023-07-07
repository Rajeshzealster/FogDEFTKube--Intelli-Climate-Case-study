#import RPi.GPIO as GPIO
import os
import paho.mqtt.client as mqtt
import json
# MQTT broker settings
broker_address = os.getenv('BROKER_ADDRESS', '192.168.0.251')
broker_port = int(os.getenv('BROKER_PORT', '1883'))
#broker_address = "192.168.0.251"
#broker_port = 1883
data_topic = "sensor/data"
temp_topic = "sensor/temperature"
humid_topic = "sensor/humidity"

# MQTT client initialization
client = mqtt.Client()
client.connect(broker_address, broker_port)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("Received payload: " + payload)
    data = json.loads(payload)
    temperature = data["temperature"]
    humidity = data["humidity"]
    
    if temperature > 30.0:
        client.publish(temp_topic, temperature)
        print("Published to " + temp_topic)
        
    if humidity > 70.0:
        client.publish(humid_topic, humidity)
        print("Published to " + humid_topic)

# subscribe to data topic
client.subscribe(data_topic)

# set up callback function for incoming messages
client.on_message = on_message

# start loop to listen for incoming messages
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Cleanup")
#    GPIO.cleanup()

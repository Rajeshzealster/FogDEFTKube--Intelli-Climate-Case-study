import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

AC_ON = False
WINDOW_OPEN = False
LAST_MSG_TIME_TEMP = 0
LAST_MSG_TIME_HUMID = 0
NO_MSG_TIMEOUT = 30 # seconds

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sensor/temperature")
    client.subscribe("sensor/humidity")

def on_message(client, userdata, msg):
    global AC_ON, WINDOW_OPEN, LAST_MSG_TIME_TEMP, LAST_MSG_TIME_HUMID
    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "sensor/temperature":
        if not AC_ON:
            print("Turning on AC...")
            # Add code here to turn on AC
            GPIO.setmode(GPIO.BCM)
	    #for realy 1 at pin 21
            GPIO.setup(21, GPIO.OUT)
            GPIO.output(21, GPIO.LOW)#relay open
	    print("Relay 1 ON")
            GPIO.cleanup()
            #Update the Ac status
            AC_ON = True
        LAST_MSG_TIME_TEMP = time.time()
    elif msg.topic == "sensor/humidity":
        if not WINDOW_OPEN:
            print("Opening the window...")
            # Add code here to open window
            GPIO.setmode(GPIO.BOARD) #use numbers for pins
            GPIO.setwarnings(False)
            GPIO.setup(11,GPIO.OUT)
            servo=GPIO.PWM(11,50)#pin 11, pulse 50HZ
            servo.start(0)
            #rotate left for window opening
            servo.ChangeDutyCycle(4.5)
            time.sleep(3)
            #stop rotation
            servo.ChangeDutyCycle(0)
            servo.stop()
            GPIO.cleanup()
            
            
            
            
            WINDOW_OPEN = True
        LAST_MSG_TIME_HUMID = time.time()

def check_timeout():
    global AC_ON, WINDOW_OPEN, LAST_MSG_TIME_TEMP, LAST_MSG_TIME_HUMID
    if AC_ON and time.time() - LAST_MSG_TIME_TEMP > NO_MSG_TIMEOUT:
        print("Turning off AC...")
        # Add code here to turn off AC
        GPIO.setmode(GPIO.BCM)
        #for realy 1 at pin 21
        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, GPIO.HIGH)#relay close
        print("Relay 1 OFF")
        GPIO.cleanup()
        #Update the Ac status
        AC_ON = False
    if WINDOW_OPEN and time.time() - LAST_MSG_TIME_HUMID > NO_MSG_TIMEOUT:
        print("Closing window...")
        # Add code here to close window
        GPIO.setmode(GPIO.BOARD) #use numbers for pins
        GPIO.setwarnings(False)
        GPIO.setup(11,GPIO.OUT)
        servo=GPIO.PWM(11,50)#pin 11, pulse 50HZ
        servo.start(0)
        #rotate right for window closing
        servo.ChangeDutyCycle(10)
        time.sleep(3)
        #stop rotation
        servo.ChangeDutyCycle(0)
        servo.stop()
        GPIO.cleanup()
        #update the status of window
        WINDOW_OPEN = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.251", 30001, 60)

client.loop_start()

while True:
    check_timeout()
    time.sleep(1)

#Vamshi Teja
#functionalities implemented
#get attributes - cur_status(heartbeat of device), door_status, current_temperature
#set attributes - pre_heat_status,cur_temp,door_set, cur_status

#import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import json, time
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests

# device credentials
device_id        = '<DEVICE_ID>'      #  set your device id (will be the MQTT client username)
device_secret    = '<DEVICE_SECRET>'  #  set your device secret (will be the MQTT client password)
random_client_id = '<CLIENT_ID>'      #  set a random client_id (max 23 char)


# Pins Setup

'''buttonPin    = 7
ledPin       = 12
door_stat    = 21
cur_temp     = 23
cur_state    = 29
temp_set     = 31
door_set     = 33
preheat_set  = 8

GPIO.setmode(GPIO.BOARD)          # use P1 header pin numbering convention
GPIO.cleanup()                    # clean up resources
GPIO.setup(door_stat, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(cur_temp, GPIO.IN)
GPIO.setup(cur_state, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(temp_set, GPIO.OUT)
GPIO.setup(door_set, GPIO.OUT)
GPIO.setup(preheat_set,  GPIO.OUT)'''

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

#to read analog values
'''def RC_Analog (Pin):  
  counter = 0  
  # Discharge capacitor  
  GPIO.setup(Pin, GPIO.OUT)  
  GPIO.output(Pin, GPIO.LOW)  
  time.sleep(0.1)  
  GPIO.setup(Pin, GPIO.IN)  
  # Count loops until voltage across capacitor reads high on GPIO  
  while(GPIO.input(Pin)==GPIO.LOW):  
        counter =counter+1  
  return counter
'''

# Callback events #

# connection event
'''def on_connect(client, data, flags, rc):
    print('Connected, rc: ' + str(rc))

# subscription event
def on_subscribe(client, userdata, mid, gqos):
    print('Subscribed: ' + str(mid))'''

# received message event
def on_message():
    # get the JSON message
   ''' json_data = msg.payload
    # check the status property value
    print(json_data)
    door_set = json.loads(json_data)['oven'][0]['door_set']
    temp_set = json.loads(json_data)['oven'][1]['temp_set']
    preheat_set = json.loads(json_data)['oven'][0]['preheat_set']'''
   while 1<2:
        r=requests.get('http://192.168.1.138:4000/door_stat')
        soup1 = BedautifulSoup(r.text, 'html.parser')
        soup3=str(soup1)
        if soup3 == "1":
            #door_set = GPIO.HIGH
            GPIO.output(16,True)
        if soup3 == "0":
            #led_status = GPIO.LOW
            GPIO.output(16,False)
        r=requests.get('http://192.168.1.138:4000/preheat_stat')
        soup1 = BeautifulSoup(r.text, 'html.parser')
        soup3=str(soup1)
        if preheat_set == "1":
            #door_set = GPIO.HIGH
            GPIO.output(20, True)
        if preheat_set == "0":
            #door_set = GPIO.HIGH
            GPIO.output(20, False)
         
        r=requests.get('http://192.168.1.138:4000/oven_stat')
        soup1 = BeautifulSoup(r.text, 'html.parser')
        soup3=str(soup1)
        if(door_set == "0"):
            #led_status = GPIO.LOW
            GPIO.output(21, False)
        if(door_set == '1'):
            #led_status = GPIO.HIGH
            GPIO.output(21, True)
        #print(temp_set)

    # confirm changes to 
    #client.publish(out_topic, json_data)

on_message()



# MQTT settings #

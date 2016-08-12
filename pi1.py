import requests
from bs4 import BeautifulSoup

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
#, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def run():
    while 1<2:
        print("while")
        #GPIO.output(18,False)
        i=0
        for i in range(1000):
            i=i+1
        r=requests.get('http://192.168.1.138:4000/door_set')
        soup1=BeautifulSoup(r.text,'html.parser')
        soup3=str(soup1)
        if soup3=="1":
            print ("if")
            GPIO.output(18,True)
        else:
            print ("else")
            GPIO.output(18,False)
        
        
                

run()    

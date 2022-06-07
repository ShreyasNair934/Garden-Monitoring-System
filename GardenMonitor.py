import requests
import string
import serial
from picamera import PiCamera
import RPi.GPIO as GPIO
from filestack import Client
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         
camera = PiCamera()
client = Client("apiKey")
serialMonitor=serial.Serial('/dev/ttyUSB0', 9600)

def security_alert(): 
       camera.capture("/tmp/image.jpg") 
       new_filelink = client.upload(filepath="/tmp/image.jpg") 
       print(new_filelink.url)
       request = requests.post("https://maker.ifttt.com/trigger/trigger/json/with/key/bRYWwt8Ei0mPPIaQPnMBY8", json={"value1" : new_filelink.url})
       if request.status_code == 200:
        print("Alert has been Sent")
       else:
        print("Error in sending")


def moisture_alert(): 
       request = requests.post("https://maker.ifttt.com/trigger/SoilMoistureLow/json/with/key/apikey", json={"value1" : "Please Water your plant"})
       if request.status_code == 200:
        print("Alert has been Sent")
       else:
        print("Error in sending")


while True:
    input=GPIO.input(11)
    if input==0:                 
        print ("No intruders",i)
        time.sleep(0.1)
    elif input==1:               
        print("Intruder detected",i)
        camera.resolution = (1920, 1080)
        camera.start_preview()
        time.sleep(2)
        security_alert()
        camera.stop_preview()
        time.sleep(5)
    
    serialdata=serialMonitor.readline() 
    print(serialdata)
    
    if(int(serialdata)<300):
        moisture_alert()
    else:
        print("Moisture Good")
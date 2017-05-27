from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor
import time
import os

pir = MotionSensor(4)
camera= PiCamera()
RecordDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))

file_object = open("path.txt")
RPath = file_object.read()
file_object.close()

def AutoCapture(CaptureAmount, CaptureGap):
    DayFolder()
    while True:
        try:
            print("Ready!")
            if pir.motion_detected:
                CaptureCount = 1
                CaptureTime = time.strftime('%H%M%S',time.localtime(time.time()))
                print("DETECTED at %s" %(CaptureTime))
                for CaptureCount in range(1,CaptureAmount + 1):
                    CaptureTime = time.strftime('%H%M%S',time.localtime(time.time()))
                    camera.capture('%s%s/%s.jpg' %(RPath,RecordDate,CaptureTime))
                    print('photo no.%s CAPTURED as %s.jpg' %(CaptureCount, CaptureTime))
                    if CaptureCount < CaptureAmount:
                        sleep(CaptureGap)
        except (KeyboardInterrupt, SystemExit):
            break
    

def RRecord(VideoLength):
    RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))
    DayFolder()
    while True:
        try:
            camera.start_recording('%s%s/%s.h264' %(RPath,RecordDate,RecordTime))
            for i in range(1, VideoLength + 1):
                print(i)
                sleep(1)
        except (KeyboardInterrupt, SystemExit):
            break
        RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))
        camera.stop_recording()
    camera.stop_recording()

def SetPath():
    TPath = input("Enter the full new directory path to store the video: ")
    if TPath[-1] != "/":
        TPath = TPath + "/"
    global RPath
    RPath = TPath
    file_object = open("path.txt", 'w')
    file_object.write(TPath)
    file_object.close()
    DayFolder()

def DayFolder():
    file_object = open("path.txt")
    RPath = file_object.read()
    file_object.close()
    if os.path.exists('%s%s' %(RPath,RecordDate)) == False:
        os.makedirs('%s%s' %(RPath,RecordDate))

while True:
    command = input("please enter the command: ")
    if command == "record":
        RRecord(int(input("Enter the video's length: ")))
    if command == "path":
        SetPath()
    if command == "checkpath":
        print(RPath)
    if command == "auto":
        CaptureAmount = int(input("How many times you want to capture when sensor activated: "))
        CaptureGap = int(input("What is the gap(in second) between each picture capturing: "))
        AutoCapture(CaptureAmount, CaptureGap)

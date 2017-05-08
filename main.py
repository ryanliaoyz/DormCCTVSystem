from picamera import PiCamera
from time import sleep
import time
import os

camera= PiCamera()
RecordDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))

file_object = open("path.txt")
RPath = file_object.read()
file_object.close()

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
    TPath = input("Enter the full new directory path to store the video:")
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
        RRecord(int(input("Enter the video's length:")))
    if command == "path":
        SetPath()
    if command == "checkpath":
        print(RPath)

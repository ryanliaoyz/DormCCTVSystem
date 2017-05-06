from picamera import PiCamera
from time import sleep
import time
import os

camera= PiCamera()
RecordDate = time.strftime('%Y-%m-%d',time.localtime(time.time()))
RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))


def RRecord(VideoLength):
    RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))
    while True:
        try:
            camera.start_recording('/media/pi/27B7-B905/vc/%s/%s.h264' %(RecordDate,RecordTime))
            for i in range(1, VideoLength + 1):
                print(i)
                sleep(1)
        except (KeyboardInterrupt, SystemExit):
            break
        RecordTime = time.strftime('%H%M%S',time.localtime(time.time()))
        camera.stop_recording()
    camera.stop_recording()

while True:
    if os.path.exists('/media/pi/27B7-B905/vc/%s' %(RecordDate)) == False:
        os.makedirs('/media/pi/27B7-B905/vc/%s' %(RecordDate))
    RRecord(int(input("Enter the video's length:")))

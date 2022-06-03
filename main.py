#imports
from HandDetectionModule import HandDetector
import pyautogui
import pydirectinput 
import Vector
import time
from typing import Optional
from ctypes import wintypes , windll , create_unicode_buffer
import cv2

print("Running")

# a method to get the current foreground window
def getForegroundWindow():
    hwnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hwnd)
    buff = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    if buff.value:
        return buff.value
    else:
        return None

# main function
def detector():
    ptime = 0 # previous time of the hand
    ctime = 0 # current time of the hand
    cam = cv2.VideoCapture(0) # camera
    detector = HandDetector() # hand detector
    MouseDestinationx , MouseDestinationy = None , None # mouse destination
    CursorSpeed = 0.000005 # cursor speed
    pdistance = 0 # previous distance between landmarks
    MouseSpeedX , MouseSpeedY = 640,480 #cv 2 window size

    CursorRestRadius = 60

    pydirectinput.MINIMUM_DURATION = 0.000001 # minimum duration of the cursor movement
    pydirectinput.PAUSE = 0 # pause time
    pydirectinput.FAILSAFE = False # failsafe

    while True:
        # if current foreground window is the one we want
        if getForegroundWindow() == "Motion Tracking Game" or getForegroundWindow() == "Motion Tracker":
            try:
                cv2.destroyWindow("Motion Tracker (Game Unfocused)")
            except:
                pass
            _ , img = cam.read() # read the camera
            img = detector.Find(img) # find the hand
            ctime = time.time() # get the current time
            fps = 1/(ctime-ptime) # calculate the fps
            ptime=ctime 
            lm = detector.FindPosition(img) # find the landmarks
        
            img = cv2.flip(img , 1) # flip the image
            cv2.putText(img , str(int(fps)) , (10,70) , cv2.FONT_HERSHEY_COMPLEX,3 , (0,255,0) , 3) # put the fps on the image
            
            if len(lm) > 0:# if a hand is detected
                MiddleFinger = Vector.Vector3(lm[12][1] , lm[12][2] , 0) # middle finger
                FirstFinger = Vector.Vector3(lm[8][1] , lm[8][2] , 0) # index finger
                Distance = MiddleFinger.Distance(FirstFinger)/100 # distance between the two fingers

                if Distance < pdistance/2: # if the distance is smaller than the previous distance
                    print("Click")
                    pydirectinput.click()

                Cx = Vector.clamp(0.75*lm[9][1]/MouseSpeedX , 0 , 1) # clamp the x position
                Cy = Vector.clamp(0.75*lm[9][2]/MouseSpeedY , 0 , 1) # clamp the y position
                pdistance = Distance # set the previous distance
                MouseDestinationx = pyautogui.size()[0]-(Cx * pyautogui.size()[0]) # set the mouse destination
                MouseDestinationy = Cy * pyautogui.size()[1] 
                # move the cursor towards destination
                pydirectinput.moveTo(int(MouseDestinationx) , int(MouseDestinationy) , CursorSpeed , _pause=False)
            
            # relative way of moving cursor not finished
            '''if len(lm) > 0:
                MiddleFinger = Vector.Vector3(lm[12][1] , lm[12][2] , 0)
                FirstFinger = Vector.Vector3(lm[8][1] , lm[8][2] , 0)
                Distance = MiddleFinger.Distance(FirstFinger)/100
                if Distance < pdistance/2:
                    print("Click")
                    pydirectinput.click()
                pdistance = Distance
                
                MidXDistance = MouseSpeedX/2
                MidYDistance = MouseSpeedY/2
                CurrentPosition = (lm[9][1] , lm[9][2])

                cv2.circle(img , (int(MidXDistance) , int(MidYDistance)) , 60 , (150,150,150) , -1)

                XDistanceFromMid = abs(MidXDistance - CurrentPosition[0])
                YDistanceFromMid = abs(MidYDistance - CurrentPosition[1])
                
                if XDistanceFromMid > CursorRestRadius:
                    XSpeedMultiplier = abs(XDistanceFromMid - CursorRestRadius)
                    YSpeedMultiplier = abs(YDistanceFromMid - CursorRestRadius)

                    if XDistanceFromMid > CurrentPosition[0]:
                        XOffset = Vector.clamp(XSpeedMultiplier * 1 , 0 , 20)
                    else:
                        XOffset = Vector.clamp(XSpeedMultiplier * -1 , -20 , 0)

                    if YDistanceFromMid > CurrentPosition[1]:
                        YOffset = Vector.clamp(YSpeedMultiplier * -1 , -20 , 0)
                    else:
                        YOffset = Vector.clamp(YSpeedMultiplier * 1 , 0 , 20)
                    print(XOffset , YOffset)
                    pydirectinput.move(int(XOffset) , int(YOffset) , CursorSpeed , _pause=False)

                else:
                    XSpeedMultiplier = 0
                    YSpeedMultiplier = 0'''
                
            cv2.imshow("Motion Tracker" , img) # show the image
            MouseSpeedX = cv2.getWindowImageRect('Motion Tracker')[2] # get the window size
            MouseSpeedY = cv2.getWindowImageRect('Motion Tracker')[3]
            if cv2.waitKey(1) & 0xFF == ord('q'): # if q is pressed
                break
            cv2.waitKey(1)
        else:
            try:
                cv2.destroyWindow("Motion Tracker") # if the current foreground window is not the one we want
            except:
                pass
            _ , img = cam.read()
            img = detector.Find(img) 
            img = cv2.flip(img , 1)
            cv2.imshow("Motion Tracker (Game Unfocused)" , img) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cv2.waitKey(1)

    cam.release() # release the camera
    cv2.destroyAllWindows() # destroy all the windows
        
if __name__ == "__main__":
    detector()
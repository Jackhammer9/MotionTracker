import cv2

from HandDetection.HandDetectionModule import HandDetector
from HandDetection.FistDetection import FistDetection , Punched , Shield

import time
import json

def detector():
    WINDOWLESS_DETECTION = False
    ptime = 0
    ctime = 0
    cam = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        data = {}
        _ , img = cam.read()
        img = detector.Find(img)
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime=ctime 
        lm = detector.FindPosition(img)

        if not WINDOWLESS_DETECTION:
            img = cv2.flip(img , 1)
            cv2.putText(img , str(int(fps)) , (10,70) , cv2.FONT_HERSHEY_COMPLEX,3 , (0,255,0) , 3) # put the fps on the image

        if lm:
            if FistDetection(lm)[0] == 2 and FistDetection(lm)[1]:
                data['Fist_Locked'] = True
                if Shield(lm):
                    data['shield'] = True
                else:
                    data['shield'] = False
                if Punched(lm):
                    data['Punched'] = True
                    print('Punched')
                else:
                    data['Punched'] = False
            else:
                data['Fist_Locked'] = False
                data['Punched'] = False
                data['shield'] = False
        else:
            data['Fist_Locked'] = False
            data['Punched'] = False
            data['shield'] = False

        if not WINDOWLESS_DETECTION:    
            cv2.imshow("Motion Tracker" , img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        with open('data.json' , 'w') as f:
            json.dump(data , f)
            f.close()
        cv2.waitKey(1)

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detector()

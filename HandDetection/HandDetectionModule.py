import cv2 
import mediapipe

class HandDetector:

    def __init__(self):
        self.hands = mediapipe.solutions.hands
        self.Hands = self.hands.Hands()
        self.mpdraw = mediapipe.solutions.drawing_utils

    def Find(self,img,draw = True):
        RGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        self.results = self.Hands.process(RGB)

        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img , hand , self.hands.HAND_CONNECTIONS)
        return img

    def FindPosition(self,img):
        landmarks = []
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                for id , ln in enumerate(hand.landmark):
                            h , w , c = img.shape
                            cx , cy = int(ln.x*w), int(ln.y*h)
                            landmarks.append([id , cx , cy])
                            if id in [12,8]:
                                cv2.circle(img , (cx , cy) ,5 , (0,255,0) , -1)
                            elif id in [9]:
                                cv2.circle(img , (cx , cy) ,5 , (0,0,255) , -1)
        return landmarks
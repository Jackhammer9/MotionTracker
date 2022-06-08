from Vector import Vector3

INDEX_COLLISION_OLD = 0
MIDDLE_COLLISION_OLD = 0
THUMB_COLLISION_OLD = 0
RING_COLLISION_OLD = 0
PINKY_COLLISION_OLD = 0

INDEX_COLLISION_OLD_FIRST = 0
MIDDLE_COLLISION_OLD_FIRST = 0
THUMB_COLLISION_OLD_FIRST = 0
RING_COLLISION_OLD_FIRST = 0
PINKY_COLLISION_OLD_FIRST = 0
INDEX_COLLISION_OLD_SECOND = 0
MIDDLE_COLLISION_OLD_SECOND = 0
THUMB_COLLISION_OLD_SECOND = 0
RING_COLLISION_OLD_SECOND = 0
PINKY_COLLISION_OLD_SECOND = 0

PreviousFistDistance = 0
PreviousShieldDistance = 100000

def FistDetection(lm):

        global INDEX_COLLISION_OLD
        global MIDDLE_COLLISION_OLD
        global THUMB_COLLISION_OLD
        global RING_COLLISION_OLD
        global PINKY_COLLISION_OLD

        CONFIDENCE_LEVEL = 0

        if len(lm) < 25:
            INDEX_LOWER_LANDMARK = Vector3(lm[5][1] , lm[5][2] , 0)
            INDEX_UPPER_LANDMARK = Vector3(lm[8][1] , lm[8][2] , 0)

            MIDDLE_LOWER_LANDMARK = Vector3(lm[9][1] , lm[9][2] , 0)
            MIDDLE_UPPER_LANDMARK = Vector3(lm[12][1] , lm[12][2] , 0)

            RING_LOWER_LANDMARK = Vector3(lm[13][1] , lm[13][2] , 0)
            RING_UPPER_LANDMARK = Vector3(lm[16][1] , lm[16][2] , 0)

            PINKY_LOWER_LANDMARK = Vector3(lm[17][1] , lm[17][2] , 0)
            PINKY_UPPER_LANDMARK = Vector3(lm[20][1] , lm[20][2] , 0)

            THUMB_LOWER_LANDMARK = Vector3(lm[4][1] , lm[4][2] , 0)
            MIDDLE_THUMB_LANDMARK = Vector3(lm[6][1] , lm[6][2] , 0)

            INDEX_COLLISION_NEW = INDEX_LOWER_LANDMARK.Distance(INDEX_UPPER_LANDMARK)
            MIDDLE_COLLISION_NEW = MIDDLE_LOWER_LANDMARK.Distance(MIDDLE_UPPER_LANDMARK)
            RING_COLLISION_NEW = RING_LOWER_LANDMARK.Distance(RING_UPPER_LANDMARK)
            PINKY_COLLISION_NEW = PINKY_LOWER_LANDMARK.Distance(PINKY_UPPER_LANDMARK)
            THUMB_COLLISION_NEW = THUMB_LOWER_LANDMARK.Distance(MIDDLE_THUMB_LANDMARK)

            if INDEX_COLLISION_NEW < INDEX_COLLISION_OLD*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                INDEX_COLLISION_OLD = INDEX_COLLISION_NEW

            if MIDDLE_COLLISION_NEW < MIDDLE_COLLISION_OLD*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                MIDDLE_COLLISION_OLD = MIDDLE_COLLISION_NEW
            
            if RING_COLLISION_NEW < RING_COLLISION_OLD*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                RING_COLLISION_OLD = RING_COLLISION_NEW
            
            if PINKY_COLLISION_NEW < PINKY_COLLISION_OLD*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                PINKY_COLLISION_OLD = PINKY_COLLISION_NEW

            if THUMB_COLLISION_NEW < THUMB_COLLISION_OLD*3/4 :
                CONFIDENCE_LEVEL += 1
            else:
                THUMB_COLLISION_OLD = THUMB_COLLISION_NEW

            if CONFIDENCE_LEVEL >= 4:
                Fist_Mode = True
            else:
                Fist_Mode = False
        
            return (1,Fist_Mode)

        else:
            global INDEX_COLLISION_OLD_FIRST
            global MIDDLE_COLLISION_OLD_FIRST
            global THUMB_COLLISION_OLD_FIRST
            global RING_COLLISION_OLD_FIRST
            global PINKY_COLLISION_OLD_FIRST

            global INDEX_COLLISION_OLD_SECOND
            global MIDDLE_COLLISION_OLD_SECOND
            global THUMB_COLLISION_OLD_SECOND
            global RING_COLLISION_OLD_SECOND
            global PINKY_COLLISION_OLD_SECOND

            INDEX_LOWER_LANDMARK_FIRST = Vector3(lm[5][1] , lm[5][2] , 0)
            INDEX_UPPER_LANDMARK_FIRST = Vector3(lm[8][1] , lm[8][2] , 0)

            MIDDLE_LOWER_LANDMARK_FIRST = Vector3(lm[9][1] , lm[9][2] , 0)
            MIDDLE_UPPER_LANDMARK_FIRST = Vector3(lm[12][1] , lm[12][2] , 0)

            RING_LOWER_LANDMARK_FIRST = Vector3(lm[13][1] , lm[13][2] , 0)
            RING_UPPER_LANDMARK_FIRST = Vector3(lm[16][1] , lm[16][2] , 0)

            PINKY_LOWER_LANDMARK_FIRST = Vector3(lm[17][1] , lm[17][2] , 0)
            PINKY_UPPER_LANDMARK_FIRST = Vector3(lm[20][1] , lm[20][2] , 0)

            THUMB_LOWER_LANDMARK_FIRST = Vector3(lm[4][1] , lm[4][2] , 0)
            MIDDLE_THUMB_LANDMARK_FIRST = Vector3(lm[6][1] , lm[6][2] , 0)

            INDEX_COLLISION_NEW_FIRST = INDEX_LOWER_LANDMARK_FIRST.Distance(INDEX_UPPER_LANDMARK_FIRST)
            MIDDLE_COLLISION_NEW_FIRST = MIDDLE_LOWER_LANDMARK_FIRST.Distance(MIDDLE_UPPER_LANDMARK_FIRST)
            RING_COLLISION_NEW_FIRST = RING_LOWER_LANDMARK_FIRST.Distance(RING_UPPER_LANDMARK_FIRST)
            PINKY_COLLISION_NEW_FIRST = PINKY_LOWER_LANDMARK_FIRST.Distance(PINKY_UPPER_LANDMARK_FIRST)
            THUMB_COLLISION_NEW_FIRST = THUMB_LOWER_LANDMARK_FIRST.Distance(MIDDLE_THUMB_LANDMARK_FIRST)

            INDEX_LOWER_LANDMARK_SECOND = Vector3(lm[5+21][1] , lm[5+21][2] , 0)
            INDEX_UPPER_LANDMARK_SECOND = Vector3(lm[8+21][1] , lm[8+21][2] , 0)

            MIDDLE_LOWER_LANDMARK_SECOND = Vector3(lm[9+21][1] , lm[9+21][2] , 0)
            MIDDLE_UPPER_LANDMARK_SECOND = Vector3(lm[12+21][1] , lm[12+21][2] , 0)

            RING_LOWER_LANDMARK_SECOND = Vector3(lm[13+21][1] , lm[13+21][2] , 0)
            RING_UPPER_LANDMARK_SECOND = Vector3(lm[16+21][1] , lm[16+21][2] , 0)

            PINKY_LOWER_LANDMARK_SECOND = Vector3(lm[17+21][1] , lm[17+21][2] , 0)
            PINKY_UPPER_LANDMARK_SECOND = Vector3(lm[20+21][1] , lm[20+21][2] , 0)

            THUMB_LOWER_LANDMARK_SECOND = Vector3(lm[4+21][1] , lm[4+21][2] , 0)
            MIDDLE_THUMB_LANDMARK_SECOND = Vector3(lm[6+21][1] , lm[6+21][2] , 0)

            INDEX_COLLISION_NEW_SECOND = INDEX_LOWER_LANDMARK_SECOND.Distance(INDEX_UPPER_LANDMARK_SECOND)
            MIDDLE_COLLISION_NEW_SECOND = MIDDLE_LOWER_LANDMARK_SECOND.Distance(MIDDLE_UPPER_LANDMARK_SECOND)
            RING_COLLISION_NEW_SECOND = RING_LOWER_LANDMARK_SECOND.Distance(RING_UPPER_LANDMARK_SECOND)
            PINKY_COLLISION_NEW_SECOND = PINKY_LOWER_LANDMARK_SECOND.Distance(PINKY_UPPER_LANDMARK_SECOND)
            THUMB_COLLISION_NEW_SECOND = THUMB_LOWER_LANDMARK_SECOND.Distance(MIDDLE_THUMB_LANDMARK_SECOND)

            if INDEX_COLLISION_NEW_FIRST < INDEX_COLLISION_OLD_FIRST*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                INDEX_COLLISION_OLD_FIRST = INDEX_COLLISION_NEW_FIRST

            if MIDDLE_COLLISION_NEW_FIRST < MIDDLE_COLLISION_OLD_FIRST*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                MIDDLE_COLLISION_OLD_FIRST = MIDDLE_COLLISION_NEW_FIRST

            if RING_COLLISION_NEW_FIRST < RING_COLLISION_OLD_FIRST*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                RING_COLLISION_OLD_FIRST = RING_COLLISION_NEW_FIRST

            if PINKY_COLLISION_NEW_FIRST < PINKY_COLLISION_OLD_FIRST*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                PINKY_COLLISION_OLD_FIRST = PINKY_COLLISION_NEW_FIRST

            if THUMB_COLLISION_NEW_FIRST < THUMB_COLLISION_OLD_FIRST*3/4 :
                CONFIDENCE_LEVEL += 1
            else:
                THUMB_COLLISION_OLD_FIRST = THUMB_COLLISION_NEW_FIRST

            if INDEX_COLLISION_NEW_SECOND < INDEX_COLLISION_OLD_SECOND*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                INDEX_COLLISION_OLD_SECOND = INDEX_COLLISION_NEW_SECOND

            if MIDDLE_COLLISION_NEW_SECOND < MIDDLE_COLLISION_OLD_SECOND*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                MIDDLE_COLLISION_OLD_SECOND = MIDDLE_COLLISION_NEW_SECOND

            if RING_COLLISION_NEW_SECOND < RING_COLLISION_OLD_SECOND*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                RING_COLLISION_OLD_SECOND = RING_COLLISION_NEW_SECOND

            if PINKY_COLLISION_NEW_SECOND < PINKY_COLLISION_OLD_SECOND*3/4:
                CONFIDENCE_LEVEL += 1
            else:
                PINKY_COLLISION_OLD_SECOND = PINKY_COLLISION_NEW_SECOND

            if THUMB_COLLISION_NEW_SECOND < THUMB_COLLISION_OLD_SECOND*3/4 :
                CONFIDENCE_LEVEL += 1
            else:
                THUMB_COLLISION_OLD_SECOND = THUMB_COLLISION_NEW_SECOND

            if CONFIDENCE_LEVEL >= 6:
                Fist_Mode = True
            else:
                Fist_Mode = False

            return (2,Fist_Mode)

def Punched(lm):
    global PreviousFistDistance
    
    FIRST_HAND = Vector3(lm[9][1] , lm[9][2] , 0)
    SECOND_HAND = Vector3(lm[9+21][1] , lm[9+21][2] , 0)

    DepthBetweenHands = abs(FIRST_HAND.Cross(SECOND_HAND).k)

    if DepthBetweenHands < PreviousFistDistance/2:
        PreviousFistDistance = DepthBetweenHands
        return True
    else:
        PreviousFistDistance = DepthBetweenHands
        return False

def Shield(lm):
    global PreviousShieldDistance
    
    FIRST_HAND = Vector3(lm[20][1] , lm[20][2] , 0)
    SECOND_HAND = Vector3(lm[20+21][1] , lm[20+21][2] , 0)

    Distance = FIRST_HAND.Distance(SECOND_HAND)

    if Distance < 100:
        PreviousShieldDistance = Distance
        return True
    else:
        PreviousShieldDistance = Distance
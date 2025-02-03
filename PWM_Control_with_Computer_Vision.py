#                                                           #
#                                                           #
#           PWM CONTROL WITH COMPUTER VISION                #
#                                                           #
#                      William Santos                       #


import cv2
import mediapipe as mp

video = cv2.VideoCapture(0) # find the camera of the PC

hand = mp.solutions.hands # from library mediapipe. In the case we use hand map
Hands = hand.Hands(max_num_hands=1) # Max number of hands that sw recognize. # Hand detection
mpDraw = mp.solutions.drawing_utils # Responsible to draw the ligation on the hand.

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # conveter format of imagem from camera. BRG->RGB
    results = Hands.process(imgRGB)
    handsPoints = results.multi_hand_landmarks # obtain the condinators of the hand

    if handsPoints:
        for points in handsPoints:
            print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)

    cv2.imshow("Imagem",img)
    cv2.waitKey(1)
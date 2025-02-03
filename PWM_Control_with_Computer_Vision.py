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

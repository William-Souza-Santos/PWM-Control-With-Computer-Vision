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
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # conveter format of image from camera. BRG->RGB
    results = Hands.process(imgRGB)
    handsPoints = results.multi_hand_landmarks # obtain the condinators of the hand
    h, w, _ = img.shape  # obtain dimension of image h higher w width
    pontos = []
    if handsPoints:
        for points in handsPoints:
            #(points) # is visible see the the lendmarks
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h) # variable conveter in pixel
                #cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0),2) # IS POSSIBLE TO SEE EACH NUMBER IN THE HANDLE #Debughand
                pontos.append((cx, cy))
                #print(pontos)

    dedos = [8, 12, 16, 20]  #this values are reference  in mediapipe library (left hand)

# left hand logic

    contador = 0
    if pontos:
        if pontos[4][0] < pontos[2][0] :  # lógica do dedão
            contador = +1
        for x in dedos:
            if pontos[x][1] < pontos[x - 2][1]:  # [posição : 8,12,16,20] [valor] #4 dedos mão esquerda
                contador += 1


    print(contador) # is possible to know how many fingers are lift

    cv2.imshow("Imagem",img)
    cv2.waitKey(1)
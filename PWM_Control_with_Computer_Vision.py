#                                                           #
#                                                           #
#           PWM CONTROL WITH COMPUTER VISION                #
#                                                           #
#                      William Santos                       #


import cv2
import mediapipe as mp
#import numpy as np
import serial
import time

#==================SERIAL COMUNICATION ===================#

# Configuração da porta serial - ajuste a porta conforme seu sistema
porta_serial = 'COM3'       # Windows
# porta_serial = '/dev/ttyUSB0'  # Linux
# porta_serial = '/dev/cu.usbmodem14101'  # Mac

baud_rate = 9600

try:
    arduino = serial.Serial(porta_serial, baud_rate, timeout=1)
    time.sleep(2)  # Aguarda a inicialização da comunicação


#==================SERIAL COMUNICATION ===================#

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




    # left hand logic

        dedos = [8, 12, 16, 20]  #this values are reference  in mediapipe library (left hand)



        contador = 0
        if pontos:
            if pontos[4][0] < pontos[2][0] :  # lógica do dedão
                contador = +1
            for x in dedos:
                if pontos[x][1] < pontos[x - 2][1]:  # [posição : 8,12,16,20] [valor] #4 dedos mão esquerda
                    contador += 1





        #print(contador) # is possible to know how many fingers are lift

        width, height = 300, 40
        max_counter = 100

        PWM = "0% de PWM"
        if contador == 1:
            #print("20% de PWM")
            PWM = "20% de PWM"

        if contador == 2:
            #print("40% de PWM")
            PWM = "40% de PWM"

        if contador == 3:
            #print("60% de PWM")
            PWM = "60% de PWM"

        if contador == 4:
            #print("80% de PWM")
            PWM = "80% de PWM"

        if contador == 5:
            #print("100% de PWM")
            PWM = "100% de PWM"



        cv2.rectangle(img, (90, 10), (600, 100), (255, 0, 0), -1) # add rectangle
        cv2.putText(img,str(PWM),(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5) # add um number in image


        #cv2.rectangle(img, (0,0), (width - 1, height - 1), (255, 255, 255), 1) #gray rectangle
        cv2.rectangle(img, (200,150), (500, 110), (255, 255, 255), 1) #gray rectangle


        #filled_width = int((contador*(10) / max_counter) * width) #porcentage calculus
        #def calculo_da_porcentagem(contador,max_counter,width):

        filled_width = int((contador * (20)/ max_counter) * width)
        #return  filled_width


        if filled_width > 0:
            cv2.rectangle(img, (200, 150), (200+filled_width - 1, 110), (0, 255, 0), -1)

        contador_uart= contador*20
        #print(contador_uart)

        # Envia o valor como string (ex: "20\n") int #Cast from INT to STRING
        arduino.write(f"{contador_uart}\n".encode())
        #print(f"Enviado: {contador_uart}%")
        #time.sleep(5)

        #cv2.imshow("Imagem",img)
        #cv2.waitKey(1)
        cv2.imshow("Imagem", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break


except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fecha a conexão ao sair (Ctrl+C)
    if 'arduino' in locals():
        arduino.close()
        print("Conexão serial fechada.")
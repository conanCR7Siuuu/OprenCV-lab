import cv2
import numpy as np
from matplotlib import pyplot as plt

def eventoraton(evento, x, y, flags, params):
    if evento == cv2.EVENT_LBUTTONUP:
        print("H: ", framehsv[y,x,0])
        print("S: ", framehsv[y,x,1])
        print("V: ", framehsv[y,x,2])


#histograma, (axH,axS,axV) = plt.subplots(1,3)
#plt.ion()
#plt.show()


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()

cv2.namedWindow("WEBCAM")
cv2.setMouseCallback("WEBCAM", eventoraton)
while True:
    ret, frame = cap.read()

    if not ret:
        print("No he podido leer el frame")
        break

    framehsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(framehsv)

    mbg = cv2.inRange(framehsv, (70,50,50),(90,255,255))
    mascarabg= cv2.merge((mbg,mbg,mbg))
    mascarabg = cv2.GaussianBlur(mascarabg, (5,5), 0)

    mascarabg = cv2.merge((mbg,mbg,mbg))
    mascarafg = cv2.bitwise_not(mascarabg)

    fg = cv2.bitwise_and(frame, mascarafg)
    bg = cv2.bitwise_and(frame, mascarabg)


    histoh = cv2.calcHist([framehsv], [0], None, [180], [0,180])
    histos = cv2.calcHist([framehsv], [1], None, [256], [0,256])
    histov = cv2.calcHist([framehsv], [2], None, [256], [0,256])

    #axH.clear()
    #axH.set_title("TONO")
    #axH.plot(histoh)
    #axS.clear()
    #axS.set_title("SATURACION")
    #axS.plot(histos)
    #axV.clear()
    #axV.set_title("VALOR")
    #axV.plot(histov)

    #histograma.canvas.flush_events()



    cv2.imshow('WEBCAM', frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
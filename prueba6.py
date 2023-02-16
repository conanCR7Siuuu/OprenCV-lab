import cv2
import numpy as np

cap = cv2.VideoCapture("Practica9Marzo/ronaldodrinking.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)

if not cap.isOpened():
    print("No se puede abrir el fichero")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("No he podido leer el frame")
        break

    cv2.imshow('WEBCAM', frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
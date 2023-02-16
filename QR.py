from re import T
import cv2
import numpy as np
from cv2 import aruco

DICCIONARIO = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
lena = cv2.imread("R.png")
h, w, _ = lena.shape
vlena = np.array([[0,0], [w,0], [w,h], [0,h]])

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
else:
    salir = False
while not salir:
    ret, frame = cap.read()

    if not ret:
        print("No he podido leer el frame")
        salir  =True
    else:
        #Aqui procesamos el frame
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bboxs, ids, rechazados = aruco.detectMarkers(gris, DICCIONARIO)
        if ids is not None:
            #aruco.drawDetectedMarkers(frame, bboxs, ids)
            vertices = bboxs
            for i in range(len(ids)):
                vertices = bboxs[i][0].astype(int)

                #cv2.line(frame, vertices[0], vertices[2], (0,0,255), 4)
                #cv2.line(frame, vertices[1], vertices[3], (0,0,255), 4)

                #cv2.rectangle(frame, vertices[0], vertices[3], (0,255,255), 5)

                #cv2.circle(frame, vertices[0], 10, (255,0,0), 1)

                #cv2.polylines(frame, [vertices], True, (255,255,0), 2)

                #cv2.fillConvexPoly(frame, vertices, (255,255,255))

                #cv2.putText(frame, str(ids[i]), vertices[1], cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0), 1)

                matriz, _ = cv2.findHomography(vlena, vertices)
                warplena = cv2.warpPerspective(lena, matriz, (frame.shape[1], frame.shape[0]))

                cv2.fillConvexPoly(frame, vertices, (0,0,0))

                frame = warplena + frame
        
        cv2.imshow('WEBCAM', frame )
        if cv2.waitKey(1) == ord(' '):
            salir=True

cap.release()
cv2.destroyWindow('WEBCAM')
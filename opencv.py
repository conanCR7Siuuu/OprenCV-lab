from re import T
import cv2
from cv2 import distanceTransformWithLabels
import numpy as np
from cv2 import aruco 
import camara

DICCIONARIO = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
siu = cv2.imread("siu.tiff")

h, w, _ = siu.shape
vsiu =np.array([[0,0],[w,0],[w,h],[0,h]])
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se puede abrir la cámara")
    exit()
else:

    hframe = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    wframe = int(cap.get(cv2.CAP_PROP_FRAME_WIDHT))

    matrix, roi = cv2.getOptimalNewCameraMatrix(camara.cameraMatrix, camara.distCoeffs, (wframe, hframe), 1, (wframe, hframe))

    roi_x, roi_y, roi_w, roi_h = roi


    salir = False
while not salir:
    ret, frame = cap.read()

    if not ret:
        print("No he podido leer el frame")
        salir  =True
    else:

        framerectificado = cv2.undistort(frame, camara.cameraMatrix, camara.distCoeffs, None, matrix)

        framerecortado= framerectificado[roi_y:roi_y+roi_h, roi_x: roi_x+roi_w]

        frame = framerecortado
        hframe = roi_h
        wframe = roi_w
        #Aqui procesamos el frame


        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bboxs, ids, rechazados = aruco.detectMarkers(gris, DICCIONARIO)

        for bbox in bboxs:
            cv2.cornerSubPix(gris, bbox, winSize=(3,3), zeroZone=(-1,-1), criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
                                100, 0.0001))

        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(bboxs, 0.193, matrix, camara.distCoeffs)
        
        if rvecs is not None:
            for i in range(len(rvecs)):
                frame = cv2.drawFrameAxes(frame, matrix, camara.distCoeffs, rvecs[i], tvecs[i], 0.01)
                distancia = int(np.linalg.norm(np.array(tvecs[i]), ord = 2) * 100.0)
                #print(distancia)
                puntos, _ = cv2.projectPoints(np.array([[0.0,0.0,0.0]]), rvecs[i], tvecs[i], matrix, camara.distCoeffs)

                cv2.circle(frame, puntos[0][0].astype(int), 10, (0,0,255), -1)
                cv2.putText(frame, str(distancia)+" cm", puntos[0][0].asType(int), 0, 1, (0,255,255))

        #if ids is not None:
         #   #aruco.drawDetectedMarkers(frame, bboxs)
          #  for i in range(len(ids)):
           #     vertices = bboxs[i][0].astype(int)


    	        
                #cv2.line(ventana donde queramos dibujar, punto de inicio, punto de fin, color en BGR, grosor)
                #cv2.line(frame, vertices[0], vertices[2], (0,0,255), 4)
                #cv2.line(frame, vertices[1], vertices[3], (0,0,255), 4)

                #cv2.rectangle(frame, vertices[0], vertices[3], (0,255,255), 5)
                #cv2.circle(frame, vertices[0], 10, (255,0,0), -1)

                #cv2.polylines(frame, [vertices], True, (255,255,0), 2)

                #cv2.fillConvexPoly(frame, vertices, (255,255,255)) 
                 
                  
                                 #str(ids[i])
                # cv2.putText(frame, "SIUUUUUU", vertices[1], cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)

                # matriz, _ = cv2.findHomography(vsiu, vertices)             
                
                # warpsiu = cv2.warpPerspective(siu, matriz, (frame.shape[1], frame.shape[0]))

                # cv2.fillConvexPoly(frame, vertices, (0,0,0))

                # frame = frame + warpsiu


            
        cv2.imshow('WEBCAM', frame)
        if cv2.waitKey(1) == ord(' '):
            salir=True

cap.release()
cv2.destroyWindow('WEBCAM')
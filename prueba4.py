import cv2
import numpy as np
opencv = cv2.imread('Practica9Marzo/OIP.tif')
b, g, r = cv2.split(opencv)
cv2.imshow('ROJO', r)
cv2.imshow('VERDE', g)
cv2.imshow('AZUL', b)
opencv_grb = cv2.merge((g,r,b))
cv2.imshow ('GRB', opencv_grb)
cv2.waitKey()
cv2.destroyAllWindows
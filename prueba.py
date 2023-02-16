import cv2 # Importa modulo
import numpy as np # Importa módulo como
rgb  = np.random.randint(255, size=(250,250,3), dtype=np.uint8) #Crea un array y lo rellena con numeros aleatorios
cv2.imshow('TEST', rgb) # Creamos ventana test donde ponemo la imagen
cv2.waitKey() # Espera a que pulses una tecla
cv2.destroyWindow('TEST') # Cerrar ventana
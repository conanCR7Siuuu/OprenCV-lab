import cv2
import numpy as np
import camara

img = cv2.imread("R.png")
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bn = cv2.threshold(gris,200, 255, cv2.THRESH_BINARY)

#harris = cv2.cornerHarris(bn,blockSize=5,ksize=15,k=0.01)
#harris = cv2.dilate(harris,None)
#_, harris = cv2.threshold(harris, 0.01*harris.max(), 255, cv2.THRESH_BINARY)
#harris = np.uint8(harris)
#_, _, _, centroids = cv2.connectedComponentsWithStats(harris)

#corners = cv2.goodFeaturesToTrack(bn, maxCorners=80, qualityLevel=0.001, minDistance=20, useHarrisDetector=True, k=0.01)

circulos = cv2.HoughCircles(bn, cv2.HOUGH_GRADIENT, dp=1.5, minDist=100, param1=50, param2=30)
for c in circulos:
    x, y, r= c[0].astype(int)
    cv2.circle(img, (x,y), r, (255,0,0), 2)

#poli, _ = cv2.findContours(bn, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#for p in poli:
    #vertices = cv2.approxPolyDP(p, 0.009*cv2.arcLength(p,True), True)
    #cv2.polylines(img, [vertices], (255,0,0), len(vertices))

    #x,y,w,h = cv2.boundingRect(p)
    #cv2.rectangle(img,(x,y), (x+w,y+h), (0,0,255), 2)

    #mar = cv2.minAreaRect(p)
    #box = cv2.boxPoints(mar)
    #box = cv2.astype(int)

    #(x,y), r = cv2.minEnclosingCircle(p)
    #x=int(x)
    #y=int(y)
    #z=int(z)
    #cv2.circle(img,(x,y), r, (255,0,255), 2)



#for c in corners:
#for c in centroids:
    #x = c[0].astype(int)
    ##x = c[0][0].astype(int)
    #y = c[1].astype(int)
    ##y = c[0][1].astype(int)
    #cv2.circle(img,(x,y), 6, (0,255,0),2)

cv2.imshow("ORIGINAL", img)
cv2.imshow("IMAGEN", bn)
#cv2.imshow("HARRIS", harris)

cv2.waitKey()
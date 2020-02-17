import cv2
import imutils

faceCascade = cv2.CascadeClassifier("face.xml")

cap = cv2.VideoCapture(0)
while True:
    zartZurt, colorfulSCreen = cap.read()
    colorfulSCreen = imutils.resize(colorfulSCreen, width=1500, height=120)
    colorfulSCreen = imutils.rotate(colorfulSCreen, angle=0)
    grayScreen = cv2.cvtColor(colorfulSCreen, cv2.COLOR_BGR2GRAY)

    casc = faceCascade.detectMultiScale(grayScreen, 1.3, 2)
    for (x,y,w,h) in casc:
        cv2.rectangle(colorfulSCreen,(x+5,y+5),(x+w-5,y+h-5),(0,255,0),2)

    cv2.imshow('Camera', colorfulSCreen)
    if cv2.waitKey(1) & 0xFF == ord('x'):#press x for quit
            break

cap.release()
cv2.destroyAllWindows()



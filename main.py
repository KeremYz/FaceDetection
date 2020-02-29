import cv2
import imutils

faceCascade = cv2.CascadeClassifier("face.xml")

cap = cv2.VideoCapture(0)
screenName = 'Camera'
cv2.namedWindow(screenName, cv2.WINDOW_NORMAL);
while True:
    zartZurt, colorfulScreen = cap.read()
    colorfulScreen = imutils.resize(colorfulScreen, width=1500, height=120)
    colorfulScreen = imutils.rotate(colorfulScreen, angle=0)
    grayScreen = cv2.cvtColor(colorfulScreen, cv2.COLOR_BGR2GRAY)

    casc = faceCascade.detectMultiScale(grayScreen, 1.3, 2)
    for (x, y, w, h) in casc:
        cv2.rectangle(colorfulScreen, (x + 5, y + 5), (x + w - 5, y + h - 5), (0, 255, 0), 2)

    cv2.imshow(screenName, colorfulScreen)
    key = cv2.waitKey(1)
    if key == ord('x'):  # press x for quit
        print("Gidiyorsun demek ")
        break
    if key == ord('f'):
        print("TAM EKRAN ")
        cv2.setWindowProperty(screenName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap.release()
cv2.destroyAllWindows()

import cv2 as cv
capturaVideo = cv.VideoCapture(0)
if not capturaVideo.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    tipocamara,camara = capturaVideo.read()
    grises=cv.cvtColor(camara, cv.COLOR_BGR2GRAY)

    cv.imshow("En vivo",camara)
    if cv.waitKey(1)==ord("q"):
        break
capturaVideo.release()
cv.destroyAllWindows()
import cv2 as cv

if __name__ == "__main__":
    
    import cv2 as cv

    capture = cv.VideoCapture(0)
    import cv2

    while True:
        isTrue, src = capture.read()
        grayFrame = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        
        haar_cascade = cv.CascadeClassifier("haarCascades/haarcascade_frontalface_alt.xml")
        
        faces_rect = haar_cascade.detectMultiScale(grayFrame, 1.1, 4)
        
        for (x, y, w, h) in faces_rect:
            cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 67), thickness=2)
        
        cv.imshow('Video', src)
        
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    capture.release()

    cv.destroyAllWindows()

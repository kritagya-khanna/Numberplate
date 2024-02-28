import cv2 as cv

numplatecascade=cv.CascadeClassifier('resorces/haarcascade_russian_plate_number.xml')
web=cv.VideoCapture(0)
web.set(3, 640)
web.set(4,480)
web.set(10, 200)
count=0



while True:
    _, img = web.read()


    imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    numberplates = numplatecascade.detectMultiScale(imggray,1.1,4)
    for (x,y,w,h) in numberplates:
        area=w*h
        if area>500:
            cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            cv.putText(img, "numberplate",(x,y-5), cv.FONT_ITALIC,1,(255,50,255), 1)
            imgroi=img[y:y+h,x:x+w]
            cv.imshow("numberplate", imgroi)
    cv.imshow("webcam", img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite('resorces/scanned/noplate_'+str(count)+".jpg",imgroi)
        cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
        cv.putText(img, "scan saved", (155,265),cv.FONT_HERSHEY_PLAIN,2,(255,255,0),2)
        cv.imshow("result", img)
        cv.waitKey(500)
        count+=1
        break
from pytube import YouTube
import cv2
from time import sleep

height = int(input('Высота: '))
cap = cv2.VideoCapture(YouTube(input('Ссылка на видео: ')).streams.filter(res="720p").first().download())

width = round(((cap.get(cv2. CAP_PROP_FRAME_WIDTH) / cap.get(cv2. CAP_PROP_FRAME_HEIGHT )) / (11.0/24.0)) * float(height))


print("Измените размер консоли на ", width, height)
input()

br = ' .:!/r(l1Z4H9W8$@'
max_br = len(br)-1

frames = []

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(width,height))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        view = ''
        for i in gray:
            for j in i:
                view = view + br[int(j/255*max_br)]
        frames.append(view)
        cv2.imshow('Frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    else: 
        break

for i in frames:
    print(i)
    sleep(0.016)

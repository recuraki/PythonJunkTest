import cv2
import numpy
from copy import deepcopy

cap = cv2.VideoCapture("test.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')

ret, frame = cap.read()
if len(frame.shape) == 3:
    height, width, channels = frame.shape[:3]
else:
    height, width = frame.shape[:2]
    channels = 1

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (width,height))

zeros = numpy.zeros((height, width), frame.dtype)
layer_blue = []
depth = 5

for i in range(depth):
    layer_blue.append(zeros)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(frame)

        layer_blue.append(img_blue_c1)
        layer_blue = deepcopy(layer_blue[1:])
        img_blue_c1 = deepcopy(layer_blue[0])

        frame = cv2.merge((img_red_c1, img_green_c1, img_blue_c1))

        out.write(frame)
        #cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
cap.release()

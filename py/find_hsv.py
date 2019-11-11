#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
* create by afterloe
* MIT License
* version 1.0
"""

import cv2
import numpy as np

yellow_lower=np.array([9,135,231])
yellow_upper=np.array([31,255,255])

cap=cv2.VideoCapture(0) # 读取视频
cap.set(3, 320)
cap.set(4, 240)

while 1:
    ret, frame = cap.read()
    frame= cv2.GaussianBlur(frame, (5,5), 0)
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask= cv2.inRange(hsv, yellow_lower, yellow_upper)

    mask= cv2.erode(mask, None, iterations=2)
    mask= cv2.GaussianBlur(mask, (3,3), 0)
    res= cv2.bitwise_and(frame, frame, mask=mask)
    cnts=cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts)>0:
        cnt=max(cnts, key=cv2.contourArea)
        (x,y), radius= cv2.minEnclosingCircle(cnt)
        cv2.circle(frame, (int(x), int(y)), int(radius), (255,0, 255), 2)
        print(int(x), int(y))
    else:
        pass

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(5)&0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

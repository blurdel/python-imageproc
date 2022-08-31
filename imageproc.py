from configparser import Interpolation
import cv2
import os
import numpy as np

print(os.getcwd())

try:

    path = r"images/lena.jpg"

    orig = cv2.imread(path, cv2.IMREAD_UNCHANGED) 
    
    resized = cv2.resize(orig, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    blur =  cv2.blur(orig, (5,5))

    cv2.imshow('Orig', orig)
    cv2.imshow('Gray', gray)
    cv2.imshow('Blur', blur)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(str(e))

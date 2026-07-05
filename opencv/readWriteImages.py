import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readImage(): 
    root = os.getcwd()
    imgPath = os.path.join(root,"opencv/images/1.png")
    img = cv.imread(imgPath)
    debug = 1
    cv.imshow("huha",img)
    cv.waitKey(0)

def writeImage():
    
    root = os.getcwd()
    imgPath = os.path.join(root,"opencv/images/1.png")
    img = cv.imread(imgPath)
    
    outPath = os.path.join(root,"opencv/images/output.png")
    cv.imwrite(outPath,img)
    
if __name__ == "__main__":
    # readImage()
    writeImage()
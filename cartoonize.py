import cv2
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt


img = cv2.imread('projects/cat.jpg', 1)
imgC = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bilat = cv2.bilateralFilter(imgrgb,9,150,150)
medianed = cv2.medianBlur(imgrgb, 7)
lap = cv2.Laplacian(bilat, cv2.CV_64F, ksize=3 )
lapn = np.uint8(np.absolute(lap))
lapm = cv2.Laplacian(medianed, cv2.CV_64F, ksize=3)
lapmn = np.uint8(np.absolute(lapm))

(T,th) = cv2.threshold(lapmn,125,255,cv2.THRESH_BINARY_INV)
# cv2.imshow('img', th )
# cv2.waitKey(0)
# cv2.destroyAllWindows()



titles = ['img',  'bilateral', 'median', 'grayimage', 'laplace for bilateral', 'laplace for median',"th"]
images = [imgC, medianed, bilat,  imgrgb, lapn,  lapmn, th]

def plot(titles,images):
    if(len(images)<=2):
        x, y = 1, 2
    elif(len(images)<=4):
        x, y = 2, 2
    elif(len(images)<=6):
        x, y = 2, 3
    elif(len(images)<=9):
        x, y = 3, 3

    for i in range(len(images)):
        
        plt.subplot(x, y, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

plot(titles,images)




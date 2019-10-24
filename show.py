


import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread('projects/1567391041789.jpg', 1)
imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernal = np.ones((9, 9), np.float32)/81
# smoothing
conv2d = cv2.filter2D(imgrgb, -1, kernal)

blured  = cv2.blur(imgrgb,(5,5))


gausianblured = cv2.GaussianBlur(imgrgb, (5,5),0)

medial = cv2.medianBlur(imgrgb,5)

bilat = cv2.bilateralFilter(imgrgb,9,150,150)

#edging
lap = cv2.Laplacian(imgg, cv2.CV_64F, ksize=3 )
lap = np.uint8(np.absolute(lap))

# plt.imshow(imgrgb)

titles = ['image', 'convoloution2d' , 'blured', 'gausianblured', 'median', 'bilateral']
images = [imgrgb, conv2d, blured, gausianblured, medial, bilat]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

for(i in range(5)):
    {
        print("hi")
    }
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





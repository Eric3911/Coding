#conding: utf-8-
#Author:'Jungang'
#Time:2019/4/26

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('E:/code with life/py100/out.jpg')
H = np.float32([[1,0,100],[0,1,50]])
rows,cols = img.shape[:2]
res = cv2.warpAffine(img,H,(rows,cols)) #需要图像、变换矩阵、变换后的大小
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(res)

cv2.waitKey(0)

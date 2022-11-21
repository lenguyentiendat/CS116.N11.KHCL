import os
import cv2 as cv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

img_path = 'C:\Users\Asus\OneDrive - Trường ĐH CNTT - University of Information Technology\Máy tính\Dang_Face.jpg'
image = cv.imread(img_path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow(image)


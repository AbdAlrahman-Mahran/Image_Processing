from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np


#function to plot two images side by side
def plot_images(image_1, image_2,title_1, title_2):
    plt.subplot(1, 2, 1)
    plt.imshow(image_1)
    plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.imshow(image_2)
    plt.title(title_2)
    plt.show()

#function to plot the histogram of each of the three channels
def plot_3_channels(image,j):
    color = ('Red','Green','Blue')
    intensity_values=np.array([x for x in range(256)])

    for i,col in enumerate(color):
        plt.subplot(2,4,i+1+(j*4))
        histogram = cv2.calcHist([image],[i],None,[256],[0,256])
        if j==0:
            plt.title("Original "+col+" channel")
        else:
            plt.title("Adjusted "+col+" channel")
        plt.plot(intensity_values,histogram,color = col,label=col+" channel")
            
        plt.xlim([0,256])
        plt.legend()
        
    for i,col in enumerate(color):
        plt.subplot(2,4,(j+1)*4)
        histogram = cv2.calcHist([image],[i],None,[256],[0,256])
        
        plt.plot(intensity_values,histogram,color = col,label=col+" channel")

    plt.xlim([0,256])
    plt.legend()
    if j==0:
            plt.title("Original 3 channels")
    else:
            plt.title("Adjusted 3 channels")




image=cv2.imread('image.jpg')

image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

alpha = 1.3
beta = -50
modified_image=cv2.convertScaleAbs(image,alpha=alpha,beta=beta)

plt.figure(figsize=(10, 10))

plot_3_channels(image,0)

plot_3_channels(modified_image,1)

plt.show()

plt.figure(figsize=(10, 10))
plot_images(image,modified_image,'Original','Adjusted')





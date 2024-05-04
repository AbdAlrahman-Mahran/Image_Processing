from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np


#function to plot two images side by side
def plot_images(image_1, image_2,title_1="Orignal", title_2="New Image"):
    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    plt.imshow(image_1)
    plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.imshow(image_2)
    plt.title(title_2)
    plt.show()

#function to plot two histograms side by side
def plot_histograms(image_1, image_2,title_1="Orignal", title_2="New Image"):
    plt.figure(figsize=(9,9))
    intensity_values=np.array([x for x in range(256)])
    plt.subplot(1, 2, 1)
    plt.bar(intensity_values, cv2.calcHist([image_1],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(title_1)
    plt.xlabel('intensity')
    plt.subplot(1, 2, 2)
    plt.bar(intensity_values, cv2.calcHist([image_2],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(title_2)
    plt.xlabel('intensity')
    plt.show()

#function to plot the histogram of each of the three channels
def plot_3_channels(images):
    color = ('blue','green','red')
    intensity_values=np.array([x for x in range(256)])
    for j,image in enumerate(images):
        plt.subplot(1,2,j+1)
        for i,col in enumerate(color):
            histogram = cv2.calcHist([image],[i],None,[256],[0,256])
            plt.plot(intensity_values,histogram,color = col,label=col+" channel")
            
            plt.xlim([0,256])
            plt.legend()
        if j==0:
            plt.title("Original Histogram Channels")
        else:
            plt.title("Modified Histogram Channels")
    plt.show()


image=cv2.imread('image.jpg')

image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

alpha = 0.5
beta = 80
modified_image=cv2.convertScaleAbs(image,alpha=alpha,beta=beta)

plot_3_channels([image,modified_image])

plot_images(image,modified_image,'Original','Modified')

plot_histograms(image,modified_image,'Original','Modified')




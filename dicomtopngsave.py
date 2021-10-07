# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:26:29 2021

@author: ydadw
"""
import os,cv2
import numpy as np
import matplotlib.pyplot as plt


import pickle





with open('ConsolidatedDicom.pkl', 'rb') as file:
    img_data=(pickle.load(file))
with open('ConsolidatedDicomGT.pkl', 'rb') as file:
    ArrayDicomGT=(pickle.load(file))


path='C:\\Users\\ydadw\\Documents\\Python Scripts\\Research\\data image\\'

for i in range(0,ArrayDicomGT.shape[1]):
    filename=path+str(i)+' Age '+str(ArrayDicomGT[0,i])+' Gender '+str(ArrayDicomGT[1,i])+'.png'
    plt.imshow(img_data[:,:,i], cmap=plt.cm.bone)
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()
    
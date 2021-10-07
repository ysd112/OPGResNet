# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:35:23 2021

@author: ydadw
"""
import os,cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from keras import backend as K
#K.set_image_dim_ordering('th')

import keras 
from keras import layers

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.normalization import BatchNormalization
from keras.layers import Conv2D  , MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
import pickle



num_epoch=250

with open('ConsolidatedDicom.pkl', 'rb') as file:
    img_data=(pickle.load(file))
with open('ConsolidatedDicomGT.pkl', 'rb') as file:
    ArrayDicomGT=(pickle.load(file))



new=np.delete(img_data,[0,32,82,99,111,126,175,200,203,257],axis=-1)

newGT=np.delete(ArrayDicomGT,[0,32,82,99,111,126,175,200,203,257],axis=-1)
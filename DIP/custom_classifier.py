from keras.datasets import cifar100 # subroutines for fetching the CIFAR-10 dataset
from keras.models import Model # basic class for specifying and training a neural network
from keras.layers import Input, Convolution2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.utils import np_utils # utilities for one-hot encoding of ground truth values
from keras.models import model_from_json

import numpy as np
import os
from scipy import misc
import matplotlib.pyplot as plt
import cv2

def classify(img):
    img=cv2.resize(img,(32,32))
    plt.imshow(np.uint8(img))
    plt.show()
    # Convert the image / images into batch format
    # expand_dims will add an extra dimension to the data at a particular axis
    # We want the input matrix to the network to be of the form (batchsize, height, width, channels)
    # Thus we add the extra dimension to the axis 0.
    img=np.array([img])
     
    # get the predicted probabilities for each class
    predictions = loaded_model.predict(img)
    print(predictions,LABELS[np.argmax(predictions[0])])

    
LABELS = ['bus', 'motorcycle', 'pickup_truck', 'streetcar']
LABELS.index('bus')
    
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model_weights.h5")
print("Loaded model from disk")
from sklearn.utils import shuffle
import os
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import gc

datalabel="try_:)"

def data_label():
    return datalabel

def MCNN_data_load(NUM_CLASSES):
   
    path_x_train = "D:/Malik/SATs/Sodium vs others/Prottrans/Train_data.npy"
    path_y_train = "D:/Malik/SATs/Sodium vs others/Prottrans/Train_labels.npy"
    print(path_x_train)
    print(path_y_train)
    x_train,y_train=data_load(path_x_train,path_y_train,NUM_CLASSES)
    path_x_test = "D:/Malik/SATs/Sodium vs others/Prottrans/Test_data.npy"
    path_y_test = "D:/Malik/SATs/Sodium vs others/Prottrans/Test_labels.npy"
    print(path_x_test)
    print(path_y_test)
    x_test,y_test=data_load(path_x_test,path_y_test,NUM_CLASSES)
    path_x_independent = "D:/Malik/SATs/Sodium vs others/SLC/Independent_data.npy"
    path_y_independent = "D:/Malik/SATs/Sodium vs others/SLC/Independent_labels.npy"
    print(path_x_independent)
    print(path_y_independent)
    x_independent,y_independent=data_load(path_x_independent,path_y_independent,NUM_CLASSES)
    return(x_train,y_train,x_test,y_test,x_independent,y_independent)

def data_load(x_folder, y_folder,NUM_CLASSES,):
    x=np.load(x_folder)
    y=np.load(y_folder)
    
    x, y = shuffle(x, y, random_state=42)  # Shuffle the data
    # Reshape to add the channel dimension
    x = x.reshape(x.shape[0], 1, x.shape[1], x.shape[2])
    y= tf.keras.utils.to_categorical(y,NUM_CLASSES)
    gc.collect()
    
    return x, y
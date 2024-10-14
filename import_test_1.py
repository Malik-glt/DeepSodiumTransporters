
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
   
    path_x_train = "C:/jupyter/Malik/SodiumTransporters/Tape/Train_data.npy"
    path_y_train = "C:/jupyter/Malik/SodiumTransporters/Tape/Train_labels.npy"
    # path_x_train = "C:/jupyter/Malik/SodiumTransporters/ESM1b/All_Train_data.npy"
    # path_y_train = "C:/jupyter/Malik/SodiumTransporters/ESM1b/All_Train_labels.npy"
    # path_x_train = "C:/jupyter/Malik/SodiumTransporters/ESM2/Train_data.npy"
    # path_y_train = "C:/jupyter/Malik/SodiumTransporters/ESM2/Train_labels.npy"
    print(path_x_train)
    print(path_y_train)
    x_train,y_train=data_load(path_x_train,path_y_train,NUM_CLASSES)
    path_x_test = "C:/jupyter/Malik/SodiumTransporters/Tape/Test_data.npy"
    path_y_test = "C:/jupyter/Malik/SodiumTransporters/Tape/Test_labels.npy"
    # path_x_test = "C:/jupyter/Malik/SodiumTransporters/ESM1b/All_Test_data.npy"
    # path_y_test = "C:/jupyter/Malik/SodiumTransporters/ESM1b/All_Test_labels.npy"
    # path_x_test = "C:/jupyter/Malik/SodiumTransporters/ESM2/Test_data.npy"
    # path_y_test = "C:/jupyter/Malik/SodiumTransporters/ESM2/Test_labels.npy"
    print(path_x_test)
    print(path_y_test)
    x_test,y_test=data_load(path_x_test,path_y_test,NUM_CLASSES)

    return(x_train,y_train,x_test,y_test)

def data_load(x_folder, y_folder,NUM_CLASSES,):
    x=np.load(x_folder)
    y=np.load(y_folder)
    
    x, y = shuffle(x, y, random_state=42)  # Shuffle the data
    # Reshape to add the channel dimension
    x = x.reshape(x.shape[0], 1, x.shape[1], x.shape[2])
    y= tf.keras.utils.to_categorical(y,NUM_CLASSES)
    gc.collect()
    
    return x, y


from sklearn.utils import shuffle
import os
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import gc

datalabel = "try_:)"

def data_label():
    return datalabel

def MCNN_data_load(NUM_CLASSES):
    # Define paths for training data and labels
    # path_x_train = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/All_Train_data.npy"
    # path_y_train = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/All_Train_labels.npy"
    path_x_train = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/Train_Transporters.npy"
    path_y_train = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/Train_Trans_labels.npy"
    print(path_x_train)
    print(path_y_train)
    
    # Load training data and labels
    x_train, y_train = data_load(path_x_train, path_y_train, NUM_CLASSES)
    
    # Define paths for testing data and labels
    # path_x_test = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/All_Test_data.npy"
    # path_y_test = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/All_Test_labels.npy"
    path_x_test = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/Test_Transportrs.npy"
    path_y_test = "C:/jupyter/Malik/SodiumTransporters/ProtTrans/Test__Trans_labels.npy"
    print(path_x_test)
    print(path_y_test)
    
    # Load testing data and labels
    x_test, y_test = data_load(path_x_test, path_y_test, NUM_CLASSES)

    return (x_train, y_train, x_test, y_test)

def data_load(x_folder, y_folder, NUM_CLASSES):
    # Load embeddings and labels
    x = np.load(x_folder)
    y = np.load(y_folder)

    # Shuffle the data
    x, y = shuffle(x, y, random_state=42)
    
    # Reshape to add the channel dimension (if x has two dimensions)
    if x.ndim == 2:
        x = x.reshape(x.shape[0], 1, x.shape[1])  # Reshape if only two dimensions
    elif x.ndim == 3:
        x = x.reshape(x.shape[0], 1, x.shape[1], x.shape[2])  # Reshape if three dimensions

    # Ensure labels are in the correct format (binary)
    y = y.astype(np.int32)

    # Convert binary labels to categorical format (2 classes)
    y = tf.keras.utils.to_categorical(y, num_classes=NUM_CLASSES)

    # Cleanup to free memory
    gc.collect()
    
    return x, y
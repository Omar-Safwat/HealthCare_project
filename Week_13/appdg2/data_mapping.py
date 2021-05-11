import pandas as pd
import numpy as np
import pickle


"""
1- Go through every column in "user_data". 
2- Use column name and access dictionaries for encoding
3- Use column name and access dictionaries for decoding
"""

def encode_dataset(user_data):
    """
    Function to map data of Dtype 'object' to numerical for ML model.
    Returns an encoded DataFrame

    Args:
    ====
    user_data: A pandas DataFrame provided by the user.
    """
    #Load encoding dictionary
    with open('columns_encode.pickle', 'rb') as file:
        columns_map = pickle.load(file)

    #Using Mapping to encode data
    for col in user_data.columns:
        if str(user_data[col].dtype) == 'object':
            user_data[col] = user_data[col].map(columns_map[col])

    return user_data


def decode_dataset(user_data):
    """
    Function to map data back from numerical to 'object'
    Returns an decoded DataFrame

    Args:
    ====
    user_data: A pandas DataFrame provided by the user.
    """
    #Load decoding dictionary
    with open('columns_decode.pickle', 'rb') as file:
        columns_decode = pickle.load(file)

    #Using Mapping to encode data
    for col in user_data.columns:
        if col in columns_decode.keys():
            user_data[col] = user_data[col].map(columns_decode[col])
    
    return user_data
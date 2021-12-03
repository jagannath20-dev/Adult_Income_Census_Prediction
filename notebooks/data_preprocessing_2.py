# Import libraries
import numpy as np
import pandas as pd
import logging

logging.basicConfig(filename='logs/model_development.txt',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

# Import data
data = pd.read_csv('Dataset\adult.csv')

logging.warning('-'*100)
logging.warning('DATA_PREPROCESSING_2.')

logging.warning("Encoding 'salary' column as '<=50K':0, '>50K':1.")
data['salary'].replace({'<=50K': 0, '>50K': 1}, inplace=True, regex=True)

logging.warning("Encoding 'sex' column as 'Male':1, 'Female':0.")
data['sex'].replace({'Male': 1, 'Female': 0}, inplace=True, regex=True)

logging.warning("Encoding 'marital-status' column as 'Single':1,'Couple':0.")
data['marital-status'].replace({'Single': 1,'Couple': 0}, inplace=True, regex=True)

logging.warning("Encoding 'country' column as 'US':1,'Non-US':0.")
data['country'].replace({'US': 1, 'Non-US': 0}, inplace=True, regex=True)

logging.warning("Encoding 'employment-type' column as 'private':1,'govt':2,'self_employed':3,'without_pay':4.")
data['employment-type'].replace({'private': 1, 'govt': 2,'self_employed': 3, 'without_pay': 4}, inplace=True, regex=True)

logging.warning('data_preprocessing_2 is done.')

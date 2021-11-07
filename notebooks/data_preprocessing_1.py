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
logging.warning('DATA_PREPROCESSING_1')

# Drop rows
logging.warning("Delete rows containing '?' values init.")
data['country'] = data['country'].replace(' ?', np.nan)
data['workclass'] = data['workclass'].replace(' ?', np.nan)
data['occupation'] = data['occupation'].replace(' ?', np.nan)

data.dropna(how='any', inplace=True)

logging.warning('Data_Preprocessing_1 is done.')

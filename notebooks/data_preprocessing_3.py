# Import libraries
import numpy as np
import pandas as pd
import logging
import scipy.stats as stats

logging.basicConfig(filename='logs/model_development.txt',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

# Import data
data = pd.read_csv('Dataset\adult.csv')

# Drop columns
data.drop(['workclass', 'education', 'education-num',
           'occupation','relationship', 'race'], 
            axis=1, inplace=True)

logging.warning('-'*100)
logging.warning('DATA_PREPROCESSING_3')

logging.warning('Correlation between a binary variable and continuous variables, the point biserial correlation has been used')

for i in data.columns:
    print(i, ':', stats.pointbiserialr(data['salary'], data[i])[0])

logging.warning("Drop 'fnlwgt' and 'marital-status' columns. These columns shows negative correlation with 'salary'.")

data.drop(['fnlwgt', 'marital-status'], axis=1, inplace=True)

logging.warning('Save final dataset to reports folder')
data.to_csv('final_dataset.csv', index=False)

logging.warning('data_preprocessing_3 is done.')

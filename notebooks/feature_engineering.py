# Import Libraries
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
logging.warning('FEATURE ENGINEERING.')

logging.warning("Replacing the marital-status of ['Divorced', 'Widowed','Married-spouse-absent','Never-married','Separated'] and ['Married-AF-spouse','Married-civ-spouse'] as 'Sinlge' and 'Couple' respectively. ")

data['marital-status'] = data['marital-status'].replace(['Divorced', 'Widowed', 'Married-spouse-absent', 'Never-married', 'Separated'], 'Single', regex=True)
data['marital-status'] = data['marital-status'].replace(['Married-AF-spouse', 'Married-civ-spouse'], 'Couple', regex=True)

logging.warning("Replacing 'workclass' column with values ['Federal-gov','Local-gov','State-gov'],['Private'] ,['Self-emp-inc','Self-emp-not-inc'] and no_payment as 'govt','private' , 'self-employed' and 'without_pay' respectively.")

logging.warning('Create a function that complete the above task.')


def f(x):
    if x['workclass'] == ' Federal-gov' or x['workclass'] == ' Local-gov' or x['workclass'] == ' State-gov':
        return 'govt'
    elif x['workclass'] == ' Private':
        return 'private'
    elif x['workclass'] == ' Self-emp-inc' or x['workclass'] == ' Self-emp-not-inc':
        return 'self_employed'
    else:
        return 'without_pay'


logging.warning("Create a new column 'employment-type' that contains ['govt','private','self-employed','without_pay'] values in it.")
data['employment-type'] = data.apply(f, axis=1)

logging.warning("Replacing values in 'country' column as 'US' for United states residency and 'Non-US' for Non-United States residency")
df = [data]
for dataset in df:
    dataset.loc[dataset['country'] != ' United-States', 'country'] = 'Non-US'
    dataset.loc[dataset['country'] == ' United-States', 'country'] = 'US'

logging.warning('Feature Engineering is done.')

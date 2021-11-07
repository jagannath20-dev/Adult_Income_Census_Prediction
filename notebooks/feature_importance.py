import logging
import pandas as pd
from catboost import CatBoostClassifier


logging.basicConfig(filename='logs/model_development.txt',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.warning('-'*100)
logging.warning('FEATURE IMPORTANCE')

# dataset
data = pd.read_csv('reports/final_dataset.csv')

# Initialize the model
catboostclassifier = CatBoostClassifier(verbose=0)

logging.warning('Check features with more higher value.')
for feature in zip(data.columns, catboostclassifier.feature_importances_):
    print(feature)

logging.warning('Create a dataframe containing features and their importance.')
feature_dict = dict(zip(data.columns, list(
    catboostclassifier.feature_importances_)))
feature_df = pd.DataFrame(feature_dict, index=['Importance']).T

logging.warning("Storing 'feature_importance' dataframe to 'reports' folder.")
feature_df.to_csv('reports\feature_importance.csv', index=True)

logging.warning('Storing done.')
logging.warning('Feature importance is done.')

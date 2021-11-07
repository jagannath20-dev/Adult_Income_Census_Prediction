import numpy as np
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from collections import Counter
from imblearn.over_sampling import SMOTE
from catboost import CatBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
import pickle
import datetime
import json

logging.basicConfig(filename='logs/model_development.txt',
                    filemode='a',
                    format='%(asctime)s %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.warning('-'*100)
logging.warning('MODELLING')

logging.warning('Load final dataset')
data = pd.read_csv('reports\final_dataset.csv')

logging.warning("Store Features in 'X' variable.")
X = data.drop('salary', axis=1)

logging.warning("Store Labels in 'y' variable")
y = data['salary']

logging.warning('Split the dataset into training and testing.')
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.20,
                                                    stratify=y,
                                                    random_state=42)

print('--------Imbalanced Classification--------------')
counter = Counter(y_train)
print(counter)
logging.warning("Oversample the dataset in labels using SMOTE")
# transform
X_train, Y_train = SMOTE(random_state=42).fit_resample(X_train, y_train)

# Summarize
print('------Balanced Classification ------')
counter = Counter(Y_train)
print(counter)

logging.warning('Check the lenghts of the training and testing datasets.')
len(X_train), len(X_test), len(Y_train), len(y_test)

logging.warning('Set random seed for reproducibility.')
np.random.seed(42)

logging.warning('Initialize the model')
model = CatBoostClassifier(verbose=0)

logging.warning('Fit the training set into the model.')
model.fit(X_train, Y_train)

logging.warning('Make prediction.')
y_preds = model.predict(X_test)

logging.warning('Evaluate on test set.')
model.score(X_test, y_test)

logging.warning('Cross Validation')
rsf = RepeatedStratifiedKFold(n_splits=5,
                              n_repeats=5,
                              random_state=42)
cs = np.mean(cross_val_score(model, X, y, cv=rsf))

logging.warning('Save model using pickle.')
pickle.dump(model, open('catboost.pkl', 'wb'))

logging.warning('Load saved model')
load_pickle_model = pickle.load(open('catboost.pkl', 'rb'))

logging.warning('Make prediction using loaded model.')
preds = load_pickle_model.predict(X_test)
preds

logging.warning('Evaluation Metrics')
model_metric = {"time_stamp": datetime.now().strftime("%d-%m-%Y_%H:%M:%S"),
                "confusion_matrix": confusion_matrix(y_test, y_preds).tolist(),
                "precision": precision_score(y_test, y_preds),
                "recall": recall_score(y_test, y_preds),
                "f1_score": f1_score(y_test, y_preds)
                }

logging.warning("Save 'model_metric' to 'reports' folder in 'json' format.")

logging.warning('Modelling is done.')

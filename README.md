# Adult_Income_Census_Prediction

## 🎯Problem Statement

The Goal is to predict whether a person has an income of more than 50K a year or not. This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.

## 📝 Data Description
The dataset is downloaded from [Kaggle](https://www.kaggle.com/overload10/adult-census-dataset).
The dataset contains 15 columns and 32000+ rows.

* **age** : the age of an individual (Integer greater than 0 )
* **workclass** : a general term to represent the employment status of an individual 
     * Private, Self­emp­not­inc, Self­emp­inc, Federal­gov, Local­gov, State­gov, Without­pay, Never­worked.
* **fnlwgt**: final weight. In other words, this is the number of people the census believes the entry represents.(Integer greater than 0)
* **education**: the highest level of education achieved by an individual.
     * Bachelors, Some­college, 11th, HS­grad, Prof­school, Assoc­acdm, Assoc­voc, 9th, 7th­8th, 12th, Masters, 1st­4th, 10th, Doctorate, 5th­6th, Preschool.
* **education-num**: the highest level of education achieved in numerical form.(Integer greater than 0)
* **marital-status**: marital status of an individual. 
     * Married-civ-spouse,Never-married,Divorced,Separated,Widowed,Married-spouse-absent,Married-AF-spouse
* **occupation**: the general type of occupation of an individual
     * Tech­support, Craft­repair, Other­service, Sales, Exec­managerial, Prof­specialty, Handlers­cleaners, Machine­op­inspct, Adm­clerical,Farming­fishing,      Transport­moving, Priv­house­serv, Protective­serv,Armed­Forces.
* **relationship**: represents what this individual is relative to others. For example an individual could be a Husband. Each entry only has one relationship attribute and is somewhat redundant with marital status. We might not make use of this attribute at all
     * Wife, Own­child, Husband, Not­in­family, Other­relative, Unmarried.
* **race**: Descriptions of an individual’s race
     * White, Asian­Pac­Islander, Amer­Indian­Eskimo, Other, Black.
* **sex**: the biological sex of the individual
     * Male, Female
* **capital-gain**: capital gains for an individual (Integer greater than or equal to 0)
* **capital-loss**: capital loss for an individual (Integer greater than or equal to 0)
* **hours-per-week**: the hours an individual has reported to work per week
     * continuous.
* **native­country**: country of origin for an individual
     * United­States, Cambodia, England, Puerto­Rico, Canada, Germany, Outlying­US(Guam­USVI­etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal,Ireland, France, Dominican­Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El­Salvador, Trinadad&Tobago, Peru, Hong, Holand­Netherlands.
* **salary**: whether or not an individual makes more than $50,000 annually.
     * <=50k, >50k

## 🌲 Project Tree
```
C:.
|   info of folders.txt
|   project_tree.txt
|   
+---catboost_info
|   |   catboost_training.json
|   |   learn_error.tsv
|   |   test_error.tsv
|   |   time_left.tsv
|   |   
|   +---learn
|   |       events.out.tfevents
|   |       
|   +---test
|   |       events.out.tfevents
|   |       
|   \---tmp
+---Dataset
|       adult.csv
|       
+---logs
|       logs.txt
|       
+---notebooks
|       data_preprocessing_1.py
|       data_preprocessing_2.py
|       data_preprocessing_3.py
|       eda_and_visualization.ipynb
|       feature_engineering.py
|       feature_importance.py
|       model.py
|       
+---reports
|       feature_importance.csv
|       final_dataset.csv
|       metric.json
|       missing_value.csv
|       
+---saved_model
|       catboost.pkl
|       
\---streamlit
        app.py


```

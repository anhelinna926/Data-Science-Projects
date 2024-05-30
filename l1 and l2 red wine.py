
# Import the necessary libraries
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
import datasets

# Load the dataset
red_wine = datasets.load_dataset('codesignal/wine-quality', split='red')
red_wine = pd.DataFrame(red_wine)

# TODO: Identify the features and targets from the dataset
X = red_wine.drop(columns='quality')
y = red_wine['quality']
# TODO: Apply feature scaling to the features
scaler = StandardScaler()
X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# TODO: Fit Logistic Regression models using L1 and L2 regularization on the train data
logistic_l1 = LogisticRegressionCV(cv=5, random_state=0, penalty='l1', solver='liblinear').fit(X_train, y_train)
logistic_l2 = LogisticRegressionCV(cv=5, random_state=0, penalty='l2').fit(X_train, y_train)
# Predict the test set results
y_pred_l1 = logistic_l1.predict(X_test)
y_pred_l2 = logistic_l2.predict(X_test)

# TODO: Compute the F1 scores and print for both L1 and L2 regularizations
f1_l1 = f1_score(y_test, y_pred_l1, average='weighted')
f1_l2 = f1_score(y_test, y_pred_l2, average='weighted')
print(f'Weighted F1 Score (L1 Regularization): {round(f1_l1, 2)}')
print(f'Weighted F1 Score (L2 Regularization): {round(f1_l2, 2)}')


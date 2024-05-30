from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np

# Load the California Housing Dataset and transform it into a binary classification problem
california_data = fetch_california_housing()
X = california_data.data
Y = (california_data.target > np.median(california_data.target)).astype(int)
def run_logistic_regression(test_size):
    # TODO: Split the data into training and test sets according to the test_size parameter
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=30)
    # TODO: Instantiate and train the Logistic Regression Model on the training data
model = LogisticRegression(max_iter=1000)
    # TODO: Make predictions on the test set
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    # TODO: Print metrics for evaluation (Accuracy, Precision, Recall, F1 Score, and AUC-ROC score)
    print(f"Test Size: {test_size}")
print(f"Accuracy: {metrics.accuracy_score(Y_test, Y_pred)}")
print(f"Precision: {metrics.precision_score(Y_test, Y_pred)}")
print(f"Recall: {metrics.recall_score(Y_test, Y_pred)}")
print(f"F1 Score: {metrics.f1_score(Y_test, Y_pred)}")
Y_proba = model.predict_proba(X_test)[:, 1]
print(f"AUC ROC Score: {metrics.roc_auc_score(Y_test, Y_proba)}")
print("------------------")
# TODO: Test the Logistic Regression model with different test set sizes (0.2, 0.3, and 0.4)
run_logistic_regression(0.2)
run_logistic_regression(0.3)
run_logistic_regression(0.4)
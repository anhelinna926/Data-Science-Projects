
# Necessary import statements
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
import datasets

# Gradient Descent Function
def gradient_descent(x, y, theta, alpha, iterations):
    m = y.size
    cost_list = [] 
    theta_list = [theta] 
    
    for i in range(iterations):
        prediction = np.dot(x, theta)
        error = prediction - y
        cost = 1 / (2*m) * np.dot(error.T, error)
        cost_list.append(np.squeeze(cost))
        theta = theta - (alpha * (1/m) * np.dot(x.T, error))
        theta_list.append(theta)
    
    return theta, theta_list, cost_list
alpha =0.01
iters =1500
# TODO: Load the Red Wine Quality dataset
red_wine = datasets.load_dataset('codesignal/wine-quality', split='red')
red_wine = pd.DataFrame(red_wine)
# TODO: Select 'sulphates' as the predictive feature and 'quality' as the target variable 
x = pd.DataFrame(red_wine['sulphates'])
y = red_wine['quality']
# TODO: Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
# TODO: Initialize the model parameters to all 0
theta = np.zeros(x_train.shape[1]).reshape(-1, 1)
# TODO: Apply the Gradient Descent function to optimize the parameters
y_train = np.array(y_train).reshape(-1, 1)
g, theta_list, cost_list = gradient_descent(x_train, y_train, theta, alpha, iters)
# TODO: Create a plot to display the cost function against iterations
plt.plot(range(1, iters + 1), cost_list, color='orange')
plt.rcParams["figure.figsize"] = (10, 6)
plt.grid()
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)')
plt.title('Convergence of gradient descent on red wine dataset')
plt.show()
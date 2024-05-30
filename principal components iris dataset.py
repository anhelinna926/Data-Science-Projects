# Importing necessary libraries
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

# Loading the Iris dataset
iris = load_iris()
X = iris.data
Y = iris.target
iris_df = pd.DataFrame(data =iris.data, columns = iris.feature_names)

# TODO: Standardize the Iris dataset
scaler = StandardScaler()
X_standardized = scaler.fit_transform(iris_df)
# TODO: Perform PCA on standardized data
pca = PCA(n_components=2)
# TODO: Make a DataFrame of the transformed data (principal components)
principalComponents = pca.fit_transform(X_standardized)
# TODO: Plot the transformed data using Matplotlib's scatter plot
principalDf = pd.DataFrame(data=principalComponents, columns=['Principal Component 1', 'Principal Component 2'])
finalDf= pd.concat([principalDf, pd.DataFrame(data=iris.target, columns=['target'])], axis=1)
plt.figure(figsize=(10, 8))
plt.scatter(finalDf['Principal Component 1'], finalDf['Principal Component 2'], c=finalDf['target'], edgecolor ='k', alpha=0.6, s=150)
plt.grid(True)
plt.title('PCA Results on Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()
plt.show()
# Import the necessary libraries
from sklearn.cluster import DBSCAN
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# TODO: Standardize the features 
X = StandardScaler().fit_transform(X)
# TODO: Create a DBSCAN model and retrieve the labels
db = DBSCAN(eps=0.6, min_samples=10)
model = db.fit(X)
labels =db.labels_
# TODO: Visualize the clusters using a scatter plot showing different DBSCAN clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title(' Clustering of Iris Dataset (Standardized)')
plt.show()
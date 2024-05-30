# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# TODO: Choose 'petal length (cm)' and 'sepal width (cm)' as your features and assign to variable X
X = iris_df.iloc[:, [1, 2]].values
# TODO: Create a KMeans or KMeans++ model, customize and fit it on your feature data X
model = KMeans(n_clusters=3, init='k-means++', max_iter=100, n_init=10, random_state=0)
# TODO: Create a scatter plot with X and the predicted labels, followed by centroids
predictions = model.fit_predict(X)
plt.scatter(X[predictions == 0, 0], X[predictions == 0, 1], s=50, c='red', label='Cluster 1')
plt.scatter(X[predictions == 1, 0], X[predictions == 1, 1], s=50, c='blue', label='Cluster 2')
plt.scatter(X[predictions == 2, 0], X[predictions == 2, 1], s=50, c='green', label="Cluster 3")
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=100, c='yellow', label= 'centroids')
# TODO: Set appropriate labels and title; Create a legend and display the plot
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('KMeans Clustering on Sepal Width and Petal Length')
plt.legend()
plt.show()
# TODO: Calculate and display Silhouette Score
score = silhouette_score(X, predictions)
print(f'Silhouette Score: {score}')
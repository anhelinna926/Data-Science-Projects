
# Import required libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# TODO: Create a list to store the sum of squared distances for k=1 to 10
sse =[]
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(iris_df)
    sse.append(kmeans.inertia_)
plt.figure(figsize=(10,  8))
plt.plot(range(1, 11), sse, 'r-o')
plt.xlabel('Number of Clusters (k)', fontweight='bold')
plt.ylabel('Sum of Squared Distance', fontweight='bold')
plt.title('Show method to Determine Optimal Number of clusters', fontweight='bold')

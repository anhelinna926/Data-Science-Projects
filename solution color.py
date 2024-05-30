# Import required libraries
from sklearn import datasets
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# TODO: Initialize the t-SNE model. Make sure to highlight the local structure with the right amount of perplexity.
model = TSNE(n_components=2, random_state=0, perplexity=15, learning_rate=100)
# TODO: Fit and transform the Iris data using the t-SNE model
X_r2 = model.fit_transform(X)
# TODO: Define the colors for your plot
colors = ["r", "g", "b"]
# TODO: Create a plot to visualize the results using matplotlib. Don't forget to label each cluster with the corresponding Iris species.
for color, i in zip (colors, [0, 1, 2]):
    plt.scatter(X_r2[y == i, 0], X_r2[y == i, 1], color=color, alpha=0.8, lw=2, label=target_names[i])
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('t-SNE visualization of the Iris dataset emphasizing local structure')
# TODO: Show the plot 
plt.show()
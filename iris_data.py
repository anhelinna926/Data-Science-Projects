# Import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load Iris dataset
iris = load_iris()

# TODO: Create Iris DataFrame from iris.data and iris.feature_names
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# TODO: Standardize the dataset using StandardScaler
scaler = StandardScaler()
iris_df_standardized = scaler.fit_transform(iris_df)
# TODO: Convert the ndarray back to pandas DataFrame
iris_df_standardized = pd.DataFrame(data=iris_df_standardized, columns=iris.feature_names)
# TODO: Include 'species' back to DataFrame
iris_df_standardized['species'] = iris.target
# TODO: Print the first 5 rows of the final dataset
print(iris_df_standardized.head())


# Import the necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load the dataset
titanic_df = sns.load_dataset('titanic')
corr_matrix = titanic_df.corr(numeric_only=True)
# TODO: Calculate and visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap= 'magma')
# TODO: Show the correlation plot

# TODO: Print the correlation between 'age' and 'pclass'
print("Correlation between 'age' and 'pclass': ", corr_matrix.loc['age', 'pclass'])
# TODO: Handle redundant or correlated features; choose 'age' and 'pclass' if they are highly correlated
# TODO: If 'age' and 'pclass' are highly correlated, drop one of the columns
if abs(corr_matrix.loc['age', 'pclass']) > 0.5:
    titanic_df.drop('pclass', axis=1, inplace=True)
# TODO: Print the first 5 rows of the cleaned dataframe
print(titanic_df.head())
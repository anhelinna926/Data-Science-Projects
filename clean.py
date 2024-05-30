# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns

# TODO: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')
# TODO: Clean the dataset to remove rows with missing 'age' data
titanic_df = titanic_df.dropna(subset=['age'])
# TODO: Calculate the Z-score for the 'age' column
titanic_df['age_zscore'] = np.abs((titanic_df['age'] - titanic_df['age'].mean()) / titanic_df['age'].std())
# TODO: Identify and print outliers using the Z-score method (threshold of 3)
outliers_zscore = titanic_df[titanic_df['age_zscore'] > 3]
# TODO: Handle outliers in the 'age' column detected by the Z-score method by replacing them with a median
titanic_clean = titanic_df 
titanic_clean.loc[titanic_df['age_zscore'] > 3, 'age' ] = titanic_df['age'].median()
# TODO: Print the cleaned data
print("\nData after Handling the outliers  detected by z-score method")
print(titanic_clean)
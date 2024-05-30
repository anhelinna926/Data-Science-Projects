# Import required libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# TODO: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')
# TODO: Detect any missing values in the 'age' column and print the count
missing_values = titanic_df.isnull()
print(missing_values)
# TODO: Impute missing data in the 'age' column using backward fill
titanic_df['age'].fillna(method='bfill', inplace=True) 
# TODO: After imputing, confirm whether there are still any missing values in the 'age' column and print the count
print("\nNumber of missing values after imputation")
print(titanic_df.isnull().sum())
# TODO: Create a visualization of the missing data using seaborn's heatmap functionality
plt.figure(figsize=(10, 6))
sns.heatmap(titanic_df.isnull(), cmap='magma')
plt.show()
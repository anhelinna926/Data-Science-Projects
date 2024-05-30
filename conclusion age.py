# Import required libraries
import seaborn as sns
import numpy as np

# TODO: Load the Titanic DataSet
titanic_df = sns.load_dataset('titanic') 
# TODO: Calculate mean, median, and mode for 'age', print them
mean_age = titanic_df['age'].mean()
print(f"Mean_age: {mean_age}")
median_age = titanic_df['age'].median()
print(f"Mediam_age: {median_age}")
mode_age = titanic_df['age'].mode()[0]
print(f"Mode_age: {mode_age}")
# TODO: Calculate the standard deviation for 'age', print it
std_dev_age =np.std(titanic_df['age'])
print(f"Standart deviation of age: {std_dev_age}")
# TODO: Calculate Quartiles for 'age', print them
Q1_age_np = np.percentile(titanic_df['age'].dropna(), 25)
print(f"First quartiles of age (Numpy): {Q1_age_np}")
Q3_age_np = np.percentile(titanic_df['age'].dropna(), 75)
print(f"Third quartiles of age (Numpy): {Q3_age_np}")
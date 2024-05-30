import seaborn as sns
import numpy as np

# Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the mean, median, mode, and standard deviation for 'fare'
mean_fare = titanic_df['fare'].mean()
median_fare = titanic_df['fare'].median()
mode_fare = titanic_df['fare'].mode()[0]
std_dev_fare = np.std(titanic_df['fare'])

print(f"Mean fare: {mean_fare}")
print(f"Median fare: {median_fare}")
print(f"Mode fare: {mode_fare}")
print(f"Standard deviation of fare: {std_dev_fare}")
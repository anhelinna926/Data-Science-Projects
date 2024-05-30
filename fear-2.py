import numpy as np
import pandas as pd
import seaborn as sns

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Calculate the mean, median, and mode for the age and fare columns
mean_fare = titanic_df[['fare']].mean()
median_fare = titanic_df[[ 'fare']].median()
mode_fare = titanic_df[[ 'fare']].mode().iloc[0]

print(f"Mean of  fare: \n{mean_fare}\n")
print(f"Median fare: \n{median_fare}\n")
print(f"Mode of  fare: \n{mode_fare}\n")
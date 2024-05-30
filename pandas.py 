import pandas as pd
import numpy as np
import seaborn as sns

# Load Titanic data
titanic_df = sns.load_dataset('titanic')

# Measure of central tendency
mean_fare = titanic_df['fare'].mean()
median_fare = titanic_df['fare'].median()
mode_fare = titanic_df['fare'].mode()[0]

# Display the Measures of the central tendency
print("The Mean fare was: ", mean_fare)
print("The Median fare was: ", median_fare)
print("The Mode fare was: ", mode_fare)

# Measure of dispersion
std_dev_fare = np.std(titanic_df['fare'])

# Display the measure of dispersion
print("The Standard Deviation of fare was: ", std_dev_fare)

# Quartiles
Q1_fare = titanic_df['fare'].quantile(0.25)
Q3_fare = titanic_df['fare'].quantile(0.75)

# Display Quartiles
print("The First Quartile of fare was: ", Q1_fare)
print("The Third Quartile of fare was: ", Q3_fare)
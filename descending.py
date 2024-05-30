# Importing required libraries
import seaborn as sns
import pandas as pd

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Filter data for passengers who are older than 60 and have survived
old_survivors = titanic_df[
    (titanic_df['age'] > 60) & (titanic_df['survived'] == 1)
]

# Sort the filtered data by fare paid in descending order
sorted_data = old_survivors.sort_values('fare', ascending=False)

# Display the sorted DataFrame
print(sorted_data)
# Import required libraries
import seaborn as sns
import pandas as pd

# TODO: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')
# TODO: Filter data for third-class passengers who survived and are older than 40
filtered_data = titanic_df[(titanic_df['survived'] ==1) &
(titanic_df['pclass']==3) &
(titanic_df['age']>40)]
# TODO: Sort the filtered data by age in ascending order
sorted_data = filtered_data.sort_values('age')
# TODO: Print the sorted data
print(sorted_data)
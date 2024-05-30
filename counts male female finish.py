# Import the necessary libraries
import seaborn as sns
import pandas as pd
titanic_df = sns.load_dataset('titanic')
# TODO: Print the first 5 entries using the head function
print(titanic_df.head(5))
# TODO: Print the last 5 entries using the tail function
print(titanic_df.tail(5))
# TODO: Print a concise summary of the DataFrame using the info function
print(titanic_df.info())
# TODO: Count the number of male and female passengers using the value_counts function
print(titanic_df['sex'].value_counts())
# TODO: Print the count of unique entries in the 'embarked' column using the nunique function
print(titanic_df['embarked'].nunique())
# TODO: Print the unique entries in the 'embarked' column using the unique function
print(titanic_df['embarked'].unique())
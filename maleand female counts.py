# Importing necessary libraries
import seaborn as sns
import pandas as pd
# Loading the Titanic dataset
titanic_df = sns.load_dataset('titanic')
# Displaying the first five entries of the DataFrame
print(titanic_df.head(5))
# TODO: Display the last five entries of the DataFrame
print(titanic_df.tail(5))
# TODO: Provide a concise summary of the DataFrame
print(titanic_df.info())
# TODO: Count the number of males and females in the 'sex' column
print(titanic_df['sex'].value_counts())
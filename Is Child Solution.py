# Import the necessary libraries
import pandas as pd
import seaborn as sns

# TODO: Load the Titanic dataset into a pandas DataFrame
titanic = sns.load_dataset('titanic')
# TODO: Output the first 5 rows of the DataFrame
print(titanic.head())
# TODO: Create a new column, "IsChild", to identify the passengers who are under 18
titanic ["IsChild"] = titanic["age"].apply(lambda x: "Yes" if x < 18 else "No")
# TODO: Output the DataFrame after the addition of the 'IsChild' column
print(titanic)
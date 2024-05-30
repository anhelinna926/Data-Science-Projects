# Import the necessary libraries
import pandas as pd
import seaborn as sns

# Load the dataset
titanic = sns.load_dataset("titanic")

# Create a new column "IsChild" using a lambda function applied to the "age" column
titanic["IsChild"] = titanic["age"].apply(lambda age: "Yes" if age < 18 else "No")
titanic["IsToddler"] = titanic["age"].apply(lambda age: "Yes" if age < 5 else "No")
# Output the first 5 rows of the DataFrame
print("\nDataFrame after adding the 'IsChild' column:")
print(titanic.head(5))
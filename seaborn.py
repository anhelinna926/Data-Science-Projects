# Import the necessary libraries
import pandas as pd
import seaborn as sns

# Load the dataset
titanic = sns.load_dataset("titanic")

# Using lambda for DataFrame manipulation
# Create a new column, "IsChild", to mark the passengers who are under 18
titanic["IsChild"] = titanic["age"].apply(lambda age: "Yes" if age < 18 else "No")
print("\nDataFrame after adding the 'IsChild' column:")
print(titanic.head(5))

# New data to add - a new passenger record
new_data = pd.DataFrame({
    "survived": [1],
    "pclass": [3],
    "sex": ["male"],
    "age": [32],
    "sibsp": [0],
    "parch": [0],
    "fare": [7.75],
    "embarked": ["Q"],
    "class": ["Third"],
    "who": ["man"],
    "adult_male": [True],
    "deck": [None],
    "embark_town": ["Queenstown"],
    "alive": ["yes"],
    "alone": [True],
    "IsChild": ["No"]
})

# Concatenate the new data to the original DataFrame
titanic_concat = pd.concat([titanic, new_data], ignore_index=True)
print("\nConcatenated DataFrame:")
print(titanic_concat.tail())

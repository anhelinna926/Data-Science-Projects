import seaborn as sns
import pandas as pd

# Load Titanic dataset
titanic_df = sns.load_dataset('titanic')

# Filter passengers older than 50 and survived
old_survivors = titanic_df[
    (titanic_df['age'] > 50) & (titanic_df['survived'] == 1)
]

# TODO: Sort the survivors by fare and then by age (in descending order for both)
old_survivors_sorted = old_survivors.sort_values(['fare', 'age'], ascending=False)
# Display the first 10 rows of the sorted DataFrame
print(old_survivors_sorted.head(10))
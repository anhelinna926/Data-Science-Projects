# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import datasets

# TODO: Using the datasets library, load the 'Red Wine' part of the Wine Quality Dataset.
red_wine = datasets.load_dataset('codesignal/wine-quality', split='red')
# TODO: Convert the loaded data into a pandas DataFrame.
red_wine_df = pd.DataFrame(red_wine)
# TODO: Check if there are any missing values in the data. Print the count of missing values. Print a suitable message if there are any missing values; otherwise, print no missing ones found.
print("\nMissing values in red wine dataset:")
print(red_wine_df.isnull().sum())
plt.figure(figsize=(10, 6))
plt.hist(red_wine_df['quality'], bins=8, color='red', alpha=0.8)
plt.xlabel('Quality')
plt.ylabel('Count')
plt.title(' Distribution of Red Wine Quality:')
plt.show()
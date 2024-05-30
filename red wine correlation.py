# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datasets

# Load the Wine Quality Dataset
red_wine = datasets.load_dataset('codesignal/wine-quality', split='red')
red_wine_df = pd.DataFrame(red_wine)

# Identify the feature to be analyzed
# TODO : Calculate the correlation of 'fixed acidity' with the 'quality' of the wine
feature_corr = red_wine_df['quality'].corr(red_wine_df['fixed acidity'])
# TODO : Print the correlation 
print("\nThe correlation of 'Fixed Acidity' with 'Quality' is %.3f\n"% (feature_corr))
# TODO : Display the correlation graphically using a scatter plot
plt.figure(figsize=(10, 8))
sns.scatterplot(x='fixed acidity', y='quality', data=red_wine_df)
plt.title('Scatter Plot showing correlation between \'Quality\' and \'Fixed Acidity\' ')
plt.show()


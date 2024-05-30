# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load the Titanic dataset
titanic = sns.load_dataset('titanic')
# TODO: Create a scatter plot depicting the relationship between 'age' and 'fare', 
# distinguishing 'pclass' by hue, 'sex' by markers, and sizes based on the 'fare'.
sns.scatterplot(x= 'age', y= 'fare', hue='pclass', style= 'sex', size= 'fare', data = titanic)
# TODO: Assign a title to the plot
plt.title("Age vs Fare(Separate  markers for Sex and Fare)")
# TODO: Display the plot
plt.show()
# TODO: Calculate and print the correlation between all pairs of numerals in the dataset
corr_vals = titanic.corr(numeric_only=True)
print((corr_vals))
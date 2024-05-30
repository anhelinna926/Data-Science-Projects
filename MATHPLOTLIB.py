# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
# TODO: Load the Titanic dataset
titanic_df = sns.load_dataset('titanic')
# TODO: Set the global palette to 'Blues'
sns.set_palette('Blues')
# TODO: Use Seaborn's countplot() to create a color-coded bar plot representing gender and survival flag.
# Specify the data coordinates, color, order of 'sex' categories, and plot orientation. Also, set a title for your plot.
sns.countplot(x= 'sex', hue= 'survived', data = titanic_df, order=['male', 'female'], orient= 'v').set_title('Survived Passengers by Gender')
plt.show()

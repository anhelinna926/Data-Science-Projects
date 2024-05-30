# Importing required libraries
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Load the Titanic dataset 
titanic_df = sns.load_dataset('titanic')
# TODO: Create a boxplot to illustrate the relationship between the fare and passenger class, categorized by their survival status.
sns.boxplot(x= 'pclass', y= 'fare', hue= 'survived', order= [2, 1, 3], hue_order= [1, 0], linewidth= 1.5, whis= 1.5, color= 'skyblue', saturation= 0.8, fliersize= 5, dodge=True, palette= 'Set3', data= titanic_df )
# TODO: Set a fitting title for the plot
plt.title("Box Plot:Passengers Class vs Fare.Highlighting Survival Status")
# TODO: Finally, display the plot
plt.show()
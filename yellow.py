# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load the Titanic dataset.
titanic_df = sns.load_dataset('titanic')
# TODO: Create a histogram using Seaborn's histplot() function. Use 'age' as the variable and include KDE. Consider a bin size of 30 for granularity. 
sns.histplot(data= titanic_df, x= 'age', bins= 30, multiple= 'stack', color='Yellow', kde=True)
# TODO: Set a descriptive and engaging title for your histogram.
plt.title('The Age of Titanic Passengers')
# TODO: Clearly label your axes for better readability of the plot. 
plt.xlabel('Age')
plt.ylabel('Count')
# TODO: Display your histogram using Matplotlib's show() function.
plt.show()


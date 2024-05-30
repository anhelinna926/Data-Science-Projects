 Import the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Load the Titanic dataset and assign it to titanic_df
titanic_df = sns.load_dataset('titanic')
# TODO: Create a bar chart of the above data. Use 'purple' color, 0.7 as the alpha value, and enable grid lines
gender_data = titanic_df['sex'].value_counts()
gender_data.plot(kind='bar', color='purple', alpha=0.7, grid=True)
# TODO: Add labels and a title to the plot
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Sex distribution')
# TODO: Display the plot
plt.show()
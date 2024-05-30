# Import required libraries
import seaborn as sns
import matplotlib.pyplot as plt

# TODO: Load Titanic dataset
titanic_df = sns.load_dataset('titanic')
# TODO: Calculate the correlation matrix
correlation_matrix = titanic_df.corr(numeric_only=True)
print(correlation_matrix)
# TODO: Create a custom colormap
color_map = sns.diverging_palette( 220, 20, as_cmap=True)
# TODO: Construct a heatmap of the correlation matrix using Seaborn's heatmap() method. Annotate the heatmap, and use the custom colormap created above
sns.heatmap(correlation_matrix, annot=True, cmap= color_map)
# TODO: Display your heatmap
plt.show()
# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# TODO: Load the 'flights' dataset
flights_df = sns.load_dataset('flights')
# TODO: Pivot the DataFrame
flights_df_pivot = flights_df.pivot(index= 'month', columns= 'year', values= 'passengers')
# TODO: Get the total passenger count for each year
yearly_totals = flights_df_pivot.sum()
# TODO: Create a line plot of the total passenger count for each year with customized parameters
yearly_totals.plot(grid=True, figsize=(10, 5), linestyle= '--')
# TODO: Assign the title and labels to the plot
plt.title("Yearly Passsengers Totals (1949-1960)")
plt.ylabel("Total Passengers Count")
plt.xlabel("Year")
# TODO: Display the plot 
plt.show()
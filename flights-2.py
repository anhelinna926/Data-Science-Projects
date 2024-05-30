# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# TODO: Load the 'flights' dataset from seaborn
flights_df = sns.load_dataset('flights')
# TODO: Group the data by each month and aggregate passengers' count
month_wise_data = flights_df.groupby('month')['passengers'].sum().reset_index()
# TODO: Create a line plot with suitable parameters to visualize the distribution of passengers over the months
plt.figure(figsize=(14, 8))
plt.plot(month_wise_data['month'], month_wise_data['passengers'], marker= 'o' )
# TODO: Set the plot title, X and Y axis labels with meaningful names
plt.title('Month Wise Number of Passengers Count (1949 - 19460)', fontsize=14)
plt.xlabel('Month Wise Count', fontsize=12)
plt.ylabel('Passengers Count', fontsize=12)
# TODO: Add gridlines to the plot to improve readability
plt.grid(True)
# TODO: Finally, display the plot
plt.show()
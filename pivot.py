# Import the necessary library
import seaborn as sns

# TODO: Load the Flights dataset
flights_df = sns.load_dataset('flights')
# TODO: Calculate and print the dimensions of the dataset
print('Shape of the dataset:', flights_df.shape)
# TODO: Calculate and print the total number of records in the dataset
print('Total number of records:', len(flights_df))
# TODO: Print the first ten records of the dataset
print(flights_df.head(10))
# TODO: Print the last five records of the dataset
print(flights_df.tail(5))
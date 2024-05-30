import seaborn as sns

# TODO: Load the dataset
titanic_df = sns.load_dataset('titanic')
# TODO: Generate descriptive statistics, including all columns
titanic_stats = titanic_df.describe(include='all')
print(titanic_stats)
# TODO: Calculate the numerical data range for the 'age' column
age_range = titanic_df['age'].max() - titanic_df['age'].min()
print('Age Range:', age_range)
# TODO: Calculate the Inter Quartile Range (IQR) for the 'age' column
Q1 = titanic_df['age'].quantile(0.25)
Q3 = titanic_df['age'].quantile(0.75)
IQR = Q3-Q1
print('IQR:', IQR)
# TODO: Calculate the median of the 'age' column
median_age = titanic_df['age'].median()
print('Median Age:', median_age)
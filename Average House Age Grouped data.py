mport pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing

# Fetch the dataset
data = fetch_california_housing(as_frame=True)

# Create a DataFrame
housing_df = pd.DataFrame(data=data.data, columns=data.feature_names)

# TODO: Create categories for the 'HouseAge' feature. You can label them as 'Very New', 'New', 'Medium', 'Old', and 'Very Old'.
bins = [0, 10, 20, 30, 40, np.inf]
labels = ['Very New', 'New', 'Medium', 'Old', 'Very Old']
housing_df['Age_cat'] = pd.cut(housing_df['HouseAge'], bins=bins, labels=labels)
# TODO: Group the data by the new 'Age_cat' category and calculate the average number of bedrooms for each category.
grouped_data = housing_df.groupby('Age_cat')
average_bedrooms = grouped_data['AveBedrms'].mean()
# TODO: Print the results
print(average_bedrooms)
# TODO: Plot the result as a bar chart
average_bedrooms.plot(kind='bar', title='Average Number of Bedrooms by House Age Category' )
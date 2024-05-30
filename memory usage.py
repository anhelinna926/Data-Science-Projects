import numpy as np
import pandas as pd
from sklearn import datasets
import time

# TODO: Load the California Housing Dataset 
california_data = datasets.fetch_california_housing()
df = pd.DataFrame(data= np.c_[california_data['data'], california_data['target']], columns = california_data['feature_names'] + ['Target'])
# Function to calculate memory usage
def get_memory_usage(df):
    bytes = df.memory_usage(deep=True).sum()
    mb = bytes / 1024**2  # convert bytes to megabytes
    return mb
  
# TODO: Grab initial memory usage 
start_mem = get_memory_usage(df)
# Tune the 'MedInc' feature using Numpy and Pandas optimization techniques
start_time = time.time()
df['MedInc'] = np.log(df['MedInc'])



# TODO: Using pd.cut, cut 'MedInc' into 5 equal-sized bins and label them from 0 to 4 (0, 1, 2, 3, 4) 
labels = [0, 1, 2, 3, 4]
df['MedInc'] = pd.cut(df['MedInc'], bins=5, labels= labels)
# TODO: Finally, convert 'MedInc' into the category data type
df['MedInc'] = df['MedInc'].astype('category')
end_time = time.time()

# TODO: Compute the memory usage after tuning 
after_tuning_memory = get_memory_usage(df)
# TODO: Compute the memory reduction percentage 
memory_reduction = (( start_mem - after_tuning_memory) / start_mem) * 100
# Print the results
# TODO: Print memory usage after tuning, memory reduction percent, and time taken for optimization
print(f'Memory usage after tuning: {after_tuning_memory} MB')
print(f"Memory reduction: {memory_reduction}%")
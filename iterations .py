# Importing the necessary libraries
import time

# Define a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
  
    # Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list
    start_time=time.time()
    for _ in range(100):
        test_item in data_set
    print(f"Operation time for 'in' operation in set: {time.time() - start_time:.6f} secondf.")
    start_time = time.time()
    for _ in range(100):
        test_item in data_list
    print(f"Operation time for 'in' operation in list: {time.time() - start_time:.6f} seconds.")
# Execute the function
compare_operations()
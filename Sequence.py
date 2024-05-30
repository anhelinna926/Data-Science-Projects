# Import the necessary libraries
import pandas as pd
import numpy as np

# Creating a data set simulating bioinformatics data
data_bio = {
    "Gene": ["HP", "MPZ", "PMP22", "GJB1"],
    "Sequence": ["CAGTCA", "GACGAT", "TGCTAG", "ATGACT"],
    "Discovery_Date": pd.date_range('01/01/1950', periods=4),
    "Popularity_on_Social_Network": np.array([125, 500, 85, 200])
}
df_bio = pd.DataFrame(data_bio)
df_gene_info = pd.DataFrame(data_bio)
# TODO: Reverse the 'Sequence' entries
df_bio['Sequence'] = df_bio['Sequence'].apply(lambda x: x[::-1])
# Creating a data set simulating astronomical star data
data_astro = {
    "Star_ID": np.arange(1, 5),
    "Right_Ascension": [205.30, 64.90, 305.80, 46.5],
    "Declination": [-30.80, 39.10, -15.80, 8.30],
    "Magnitude": [2.04, 1.25, 3.17, 1.9],
    "Observation_Date": pd.date_range('06/01/2020', periods=4)
}
df_astro = pd.DataFrame(data_astro)
filter_date = pd.to_datetime('06/03/2020')

# TODO: Filter based on the 'Observation_Date'
df_astro_filtered= df_astro[df_astro['Observation_Date'] > filter_date]
# TODO: Find the most popular gene
most_popular_gene = df_bio.loc[df_bio['Popularity_on_Social_Network'].idxmax(),  'Gene']
#TODO: Output the data for bioinformatics (with reversed sequence), filtered star data, and the most popular gene
print(df_bio)
print(df_astro_filtered)
print(f"The most popular gene is: {most_popular_gene}")
#!/usr/bin/env python3

import pandas as pd
import pyreadstat

df, meta = pyreadstat.read_sav(
    "../../SPSS-Python/spss-datasets/Taste_Test_Data_File.sav"
)

# Define the data
variable_list = ["TTQ3.1_1", "TTQ3.1_2", "TTQ3.1_3"]


for variable in variable_list:
    df_list += df[variable]

# Combine the responses into a single list
responses = pd.concat([], axis=0, ignore_index=True).dropna(axis=0)

# count responses by variable value
value_counts = responses.value_counts().sort_index()
# print(value_counts)

# Calculate the percentages
percentages = (value_counts / value_counts.sum()) * 100

# Print the value counts and percentages
for value, count in value_counts.items():
    percentage = percentages[value]
    print(f"{value}: {count} ({percentage:.0f}%)")

# get total number of counts
total_counts = value_counts.sum()
print(f"Total counts: {total_counts}")

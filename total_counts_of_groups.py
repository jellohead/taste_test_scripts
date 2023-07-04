#!/usr/bin/env python3

import pandas as pd
import pyreadstat

# Read SPSS .sav file
# data, meta = pyreadstat.read_sav('input_data.sav')
data, meta = pyreadstat.read_sav(
    "../../SPSS-Python/spss-datasets/Taste_Test_Data_File.sav"
)

# List of variable names
values_list = ["TTQ3.1_1", "TTQ3.1_2", "TTQ3.1_3"]

# Select variables from the SPSS dataset
selected_variables = [
    variable for variable in meta.column_names if variable in values_list
]

# Create a new dataframe by concatenating rows
combined_df = pd.concat(
    [data[selected_var].rename(selected_var) for selected_var in selected_variables],
    axis=0,
    ignore_index=True,
).dropna(axis=0)
responses = pd.concat([Q1, Q2, Q3], axis=0, ignore_index=True).dropna(axis=0)
print(combined_df)


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

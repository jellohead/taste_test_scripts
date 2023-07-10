#!/usr/bin/env python3

import pandas as pd
import pyreadstat

# Read SPSS .sav file
data, meta = pyreadstat.read_sav(
    "../../SPSS-Python/spss-datasets/Taste_Test_Data_File.sav"
)

df_copy = pyreadstat.set_value_labels(data, meta)

# List of variable names
values_list = ["TTQ3.1_1", "TTQ3.1_2", "TTQ3.1_3"]

# Select variables from the SPSS dataset
selected_variables = [
    variable for variable in meta.column_names if variable in values_list
]

# Create a new dataframe by concatenating rows
combined_df = pd.concat(
    [df_copy[selected_var].rename(selected_var) for selected_var in selected_variables],
    axis=0,
    ignore_index=True,
).dropna(axis=0)

# count responses by variable value
value_counts = combined_df.value_counts(normalize=True).sort_index()
total_counts = combined_df.value_counts().sum()

# get total number of counts
# total_counts = value_counts.sum()
# print(value_counts)
# print(f"Total counts: {total_counts}")
print(f"{value_counts}\nTotal counts: {total_counts}")
# print(f"Total counts: {total_counts}")

# todo
# Save to Excel
# result = pd.concat([value_counts, total_counts])
# print(result)

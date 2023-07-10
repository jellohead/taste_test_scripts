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
# print(combined_df)

# Apply value formats to get meta variable value labels as rows
# value_formats = meta.variable_value_labels
# combined_df = pd.DataFrame({
#     variable: df_copy[variable].apply(lambda x: value_formats[variable].get(x, x)) for variable in selected_variables}
# )

# count responses by variable value
# value_counts = responses.value_counts().sort_index()
value_counts = combined_df.value_counts(normalize=True).sort_index()
print(value_counts)

# Calculate the percentages
# percentages = (value_counts / value_counts.sum()) * 100

# Print the value counts and percentages
# for value, count in value_counts.items():
# for value, count in combined_df.items():
# percentage = percentages[value]
# print(f"{value}: {count} ({percentages[value]:.0f}%)")
# print(f"{value}: {count}")

# get total number of counts
total_counts = value_counts.sum()
print(f"Total counts: {total_counts}")

# todo
# Save to Excel

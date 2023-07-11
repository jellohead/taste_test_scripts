#!/usr/bin/env python3
import pandas as pd
import pyreadstat
from openpyxl import load_workbook

# Read SPSS .sav file
data, meta = pyreadstat.read_sav(
    "../../SPSS-Python/spss-datasets/Taste_Test_Data_File.sav"
)

df_copy = pyreadstat.set_value_labels(data, meta)

# List of variable names
values_list = ["TTQ3.1_1", "TTQ3.1_2", "TTQ3.1_3"]

# excel file to save result to
excel_file = "../taste_test_scripts/grouped_frequencies.xlsx"

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

# count responses by variable value and get total counts for combined.df
value_counts = combined_df.value_counts(normalize=True).sort_index()
total_counts = combined_df.value_counts().sum()

print(f"{value_counts}\nTotal counts: {total_counts}")

# Save to Excel
result = pd.concat(
    [value_counts, pd.Series(total_counts, index=["Total counts"])], axis=1
)
result.columns = ["Value counts", "Total counts"]

# Open the existing workbook
book = load_workbook(excel_file)

# Create a new worksheet with the name of the first value in values_list
worksheet_name = values_list[0]

# Append the DataFrame to the existing workbook
with pd.ExcelWriter(
    "../taste_test_scripts/grouped_frequencies.xlsx",
    if_sheet_exists="overlay",
    engine="openpyxl",
    mode="a",
) as writer:
    result.to_excel(writer, sheet_name=worksheet_name, index_label="Variable")

"""
This script is designed to transform a CSV file by performing specific data manipulations.
It changes the names of 'Question' and 'Answer' columns to lowercase and removes the 'URL' column.
The script is modular, with each transformation step encapsulated in a separate function for easy maintenance and adaptability.

Functions:
- load_csv(file_path): Load a CSV file into a DataFrame.
- lowercase_column_names(df, columns): Change specified column names in a DataFrame to lowercase.
- remove_column(df, column): Remove a column from a DataFrame.
- save_csv(df, file_path): Save a DataFrame to a CSV file.
- transform_csv(input_path, output_path): Perform the entire transformation process on the CSV file.
"""

import pandas as pd

def load_csv(file_path):
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(file_path)

def lowercase_column_names(df, columns):
    """Change specified column names in a DataFrame to lowercase."""
    df.columns = [col.lower() if col in columns else col for col in df.columns]
    return df

def remove_column(df, column):
    """Remove a column from a DataFrame."""
    return df.drop(column, axis=1)

def save_csv(df, file_path):
    """Save a DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)

def transform_csv(input_path, output_path):
    """Transform the CSV file according to the specified requirements."""
    df = load_csv(input_path)
    df = lowercase_column_names(df, ['Question', 'Answer'])
    df = remove_column(df, 'URL')
    save_csv(df, output_path)

# Define file paths
input_path = '06_Data\Capstone_Data\llm_testing_results\lora_plus_rag_testing_output.csv'
output_path = 'scoring/data/rag_and_llm_output_test.csv'

# Run the transformation
transform_csv(input_path, output_path)

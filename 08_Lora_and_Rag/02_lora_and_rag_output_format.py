"""
This script transforms a CSV file by performing specific data manipulations.
It changes the names of 'Question' and 'Answer' columns to lowercase, renames 'llm_answer' to 'llm_rag_answer',
removes the 'URL' column, extracts the relevant part of each answer following "ANSWER:", and cleans up the 'answer' 
column to form a single paragraph.

Functions:
- load_csv(file_path): Load a CSV file into a DataFrame.
- lowercase_column_names(df, columns): Change specified column names in a DataFrame to lowercase.
- rename_column(df, old_name, new_name): Rename a column in a DataFrame.
- remove_column(df, column): Remove a column from a DataFrame.
- extract_answer_part(df, column): Extract the part of each answer following "ANSWER:".
- clean_answer_column(df, column): Clean up the answer column to form a single paragraph.
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

def rename_column(df, old_name, new_name):
    """Rename a column in a DataFrame."""
    df.rename(columns={old_name: new_name}, inplace=True)
    return df

def remove_column(df, column):
    """Remove a column from a DataFrame."""
    return df.drop(column, axis=1)

def split_answer(answer):
    extracted_ans = answer.split("ANSWER:\n        \n        ")[-1]
    return extracted_ans

def extract_answer_part(df, column):
    """Extract the part of each answer following 'ANSWER:'."""
    df[column] = df[column].apply(lambda x: split_answer(x))
    return df

def clean_answer_column(df, column):
    """Clean up the answer column to form a single paragraph."""
    df[column] = df[column].apply(lambda x: ' '.join(x.split()))
    return df

def save_csv(df, file_path):
    """Save a DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)

def transform_csv(input_path, output_path):
    """Transform the CSV file according to the specified requirements."""
    df = load_csv(input_path)
    df = lowercase_column_names(df, ['Question', 'Answer'])
    df = rename_column(df, 'llm_answer', 'llm_rag_answer')
    df = remove_column(df, 'URL')
    df = extract_answer_part(df, 'llm_rag_answer')
    df = clean_answer_column(df, 'llm_rag_answer')
    save_csv(df, output_path)

# Define file paths
input_path = '06_Data\Capstone_Data\llm_testing_results\lora_plus_rag_testing_output.csv'
output_path = '10_Test_and_Score/scoring/data/rag_and_llm_output_test.csv'

# Run the transformation
transform_csv(input_path, output_path)

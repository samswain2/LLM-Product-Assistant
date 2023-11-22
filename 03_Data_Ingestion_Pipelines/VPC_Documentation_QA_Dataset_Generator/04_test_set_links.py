"""
Insufficient Information Filter

This script processes a CSV file containing URLs, questions, and answers. It identifies rows where either 
the question is missing or the answer is marked as 'NOT ENOUGH INFORMATION'. These rows are filtered out, 
and their URLs are extracted into a new DataFrame. The script is designed to handle file reading and writing 
errors gracefully. It includes a configuration dictionary for easy modification of input and output file paths.

Usage:
- Set the 'input_file_path' and 'output_file_path' in the configuration dictionary.
- Run the script to filter the data and save the URLs with insufficient information to a new CSV file.
"""

import pandas as pd

def filter_insufficient_data(file_path, output_path):
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return

    try:
        # Filtering rows with missing or insufficient information
        filtered_data = data[(data['Question'].isna()) | (data['Answer'] == 'NOT ENOUGH INFORMATION')]

        # Extracting only the 'URL' column and creating a copy
        urls_to_output = filtered_data[['URL']].copy()

        # Renaming 'URL' column to 'LINK'
        urls_to_output.rename(columns={'URL': 'LINK'}, inplace=True)

        # Adding a 'Type' column with all values set to 'text-based'
        urls_to_output['Type'] = 'text-based'

        # Saving the URLs with the 'Type' column to a CSV file
        urls_to_output.to_csv(output_path, index=False)
        print(f"Filtered URLs with 'Type' column saved to: {output_path}")
    except Exception as e:
        print(f"Error processing or saving file: {e}")

# Main Execution
if __name__ == "__main__":
    # Configuration Dictionary
    config = {
        "input_file_path": "06_Data/Capstone_Data/documentation_qa_datasets/Final_Question_Answer_Pairs.csv",
        "output_file_path": "06_Data/Capstone_Data/documentation_qa_datasets/Test_Set_Links.csv"
    }

    filter_insufficient_data(config['input_file_path'], config['output_file_path'])

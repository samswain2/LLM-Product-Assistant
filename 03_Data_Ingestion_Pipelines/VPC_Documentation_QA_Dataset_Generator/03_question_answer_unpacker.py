"""
QA Pair Parser

This script parses a text file containing URL, questions, and answers into a DataFrame. 
It processes lines starting with 'URL:', 'QUESTION:', and 'ANSWER:', extracting relevant information. 
Lines with 'NOT ENOUGH INFORMATION' are also handled. The resulting DataFrame consists of columns for URL, 
Question, and Answer. The script is designed to handle errors gracefully and includes a configuration 
dictionary for easy adjustment of file paths and encoding settings.

Usage:
- Set the 'file_path', 'csv_file_path', and 'encoding' in the configuration dictionary.
- Run the script to parse the text file and optionally save the output to a CSV file.
"""

import pandas as pd

def parse_text_to_df_revised(file_path, encoding):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return pd.DataFrame(columns=['URL', 'Question', 'Answer'])
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return pd.DataFrame(columns=['URL', 'Question', 'Answer'])

    data = []
    current_url = ''

    for line in lines:
        line = line.strip()
        if line.startswith('URL:'):
            current_url = line.split('URL:')[1].strip()
        elif line.startswith('QUESTION:'):
            question = line.split('QUESTION:')[1].strip()
            answer = ''
            no_info_flag = False
        elif line.startswith('ANSWER:'):
            answer = line.split('ANSWER:')[1].strip()
            data.append([current_url, question, answer])
        elif line == 'NOT ENOUGH INFORMATION':
            no_info_flag = True
            data.append([current_url, '', 'NOT ENOUGH INFORMATION'])

    df = pd.DataFrame(data, columns=['URL', 'Question', 'Answer'])
    return df

# Main Execution
if __name__ == "__main__":
    # Configuration Dictionary
    config = {
        "file_path": "06_Data/Capstone_Data/documentation_qa_datasets/Documentation_QA_Pairs.txt",
        "csv_file_path": "06_Data/Capstone_Data/documentation_qa_datasets/Final_Question_Answer_Pairs.csv",
        "encoding": "ISO-8859-1"
    }

    df_revised = parse_text_to_df_revised(config['file_path'], config['encoding'])
    
    # Optionally, to export the DataFrame to a CSV file
    if not df_revised.empty:
        df_revised.to_csv(config['csv_file_path'], index=False)
        print(f"Data saved to {config['csv_file_path']}")

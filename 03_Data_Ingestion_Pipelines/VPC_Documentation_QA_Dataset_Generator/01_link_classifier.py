"""
VPC Link Classifier

This script classifies links from a CSV file into categories based on their content. 
It identifies if a link pertains to an 'APIReference' or contains 'API' in its description 
and classifies it as 'API'; otherwise, it classifies the link as 'text-based'. 
The classified links are then saved to a new CSV file.

The script is configured to handle errors gracefully, such as file not found or read/write errors, 
and includes a settings configuration for easy customization of input and output paths.

Usage:
- Set the 'input_file_path' and 'output_file_path' in the configuration dictionary.
- Run the script to classify the links and save them to the specified output file.
"""

import pandas as pd

def classify_link(row):
    if 'APIReference' in row['LINK'] or 'API' in row['DESC']:
        return 'API'
    else:
        return 'text-based'

def classify_vpc_links(file_path, output_path):
    try:
        # Load the dataset
        links_df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return

    # Apply classification
    try:
        links_df['Type'] = links_df.apply(classify_link, axis=1)

        # Save the updated dataset
        links_df.to_csv(output_path, index=False)
        print(f"Classified links saved to: {output_path}")
    except Exception as e:
        print(f"Error processing or saving file: {e}")

# Main Execution
if __name__ == "__main__":
    # Configuration Dictionary
    config = {
        "input_file_path": "06_Data/Capstone_Data/documentation_qa_datasets/VPC_Documentation_Links.csv",
        "output_file_path": "06_Data/Capstone_Data/documentation_qa_datasets/Classified_VPC_Links.csv"
    }

    classify_vpc_links(config['input_file_path'], config['output_file_path'])

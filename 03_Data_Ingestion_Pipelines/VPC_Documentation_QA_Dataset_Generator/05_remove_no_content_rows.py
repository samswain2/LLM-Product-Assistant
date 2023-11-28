"""
This script processes a CSV file containing question-answer pairs by filtering out rows where the 'Answer' column contains the phrase 'NOT ENOUGH INFORMATION'. It then saves the filtered data into a new CSV file.

The script operates in the following steps:
1. Load a CSV file specified by the file path.
2. Filter the DataFrame to exclude rows where the 'Answer' column matches 'NOT ENOUGH INFORMATION'.
3. Save the filtered DataFrame to a new CSV file.

Input:
- CSV file containing question-answer pairs. The file should be in a specific directory structure specified by 'file_path'.

Output:
- A new CSV file containing filtered question-answer pairs, saved to 'output_file_path'.
"""

import pandas as pd

# Load the provided CSV file
file_path = '06_Data/Capstone_Data/documentation_qa_datasets/Final_TEST_Question_Answer_Pairs.csv'
df = pd.read_csv(file_path)

# Filter out rows where any column contains 'NOT ENOUGH CONTENT'
filtered_df = df[df["Answer"] != "NOT ENOUGH INFORMATION"]

# Save the filtered DataFrame to a new CSV file
output_file_path = '06_Data/Capstone_Data/documentation_qa_datasets/Final_FILTERED_TEST_Question_Answer_Pairs.csv'
filtered_df.to_csv(output_file_path, index=False)

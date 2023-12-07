
## Overview
This folder is meant for the ETL process. `VPC_URL_Loader_and_Chunker` loads the documents from URLs, breaks the text into chunks and keep the meta data in a separate location; `VPC_Documentation_QA_Dataset_Generator`, on the other hand, is our attempt to generate Q&A pairs from the document with the help of ChatGPT.

## Directory structure 
```
├── VPC_URL_Loader_and_Chunker/ 
    ├── input_pipeline.ipynb    <- runtime
    ├── requirements.txt
    ├── sample_data.zip <- sample output file from the pipeline
├── VPC_Documentation_QA_Dataset_Generator/ obtain the test set (04->02->03->05)
    ├── 00_Ordered_Files.gitkeep
    ├── 01_link_classifier.py <- classifies links from a CSV file into categories based on their content
    ├── 02_question_answer_generator.py <- scrape web content, process it, and use OpenAI's GPT model to generate question-answer pairs based on the scraped content
    ├── 03_question_answer_unpacker.py <- parses a text file containing URL, questions, and answers into a DataFrame
    ├── 04_test_set_links.py <- processes a CSV file containing URLs, questions, and answers
    ├── 05_remove_no_content_rows.py <- processes a CSV file containing question-answer pairs by filtering out rows where the 'Answer' column contains the phrase 'NOT ENOUGH INFORMATION'
```





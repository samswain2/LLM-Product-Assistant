# Data Folder Structure for Capstone Project

This document provides an overview of the data folder structure for the Capstone Project. The structure is designed to organize the various datasets and resources required for the project.

```
├── README.md
├── Capstone_Data/
    ├── chunking.yml
    ├── chunks.zip
    ├── data.zip
    ├── ... (0 more files)
    ├── chunks/
        ├──  APIReference API_AcceptAttachment_0.txt
        ├──  APIReference API_AcceptAttachment_1.txt
        ├──  APIReference API_AcceptAttachment_2.txt
        ├── ... (5552 more files)
    ├── documentation_qa_datasets/
        ├── Classified_VPC_Links.csv
        ├── content_cache.json
        ├── Documentation_QA_Pairs.txt
        ├── ... (9 more files)
    ├── llm_testing_results/
        ├── lora_plus_rag_testing_output.csv
    ├── summaries/
        ├──  APIReference API_AcceptAttachment.txt
        ├──  APIReference API_AcceptTransitGatewayMulticastDomainAssociations.txt
        ├──  APIReference API_AcceptTransitGatewayPeeringAttachment.txt
        ├── ... (830 more files)
```

## File Description
- `README.md`: This file, containing documentation and details about the project structure and contents.

## Directory Contents

### `Capstone_Data`
This directory contains all the data files and resources used in the Capstone project.

- `chunking.yml`: Chunking data - consists of three elements per html page; chunks, link, and summary.
- `chunks.zip`: Compressed file containing the output from the chunking process.
- `data.zip`: Compressed file containing the original data sets used in the project.

#### `chunks`
Folder containing text files that are the result of the chunking process. Each file contains a piece of the larger dataset, allowing for more manageable processing. A sample of 3 files is shown, with a total of 5552 files in the directory.

#### `documentation_qa_datasets`
This folder includes datasets related to QA pairs for documentation.

- `Classified_VPC_Links.csv`: A CSV file containing classified links for VPC documentation.
- `content_cache.json`: A JSON cache file containing content data.
- `Documentation_QA_Pairs.txt`: A text file containing question and answer pairs for documentation.
- A note indicates there are 9 additional files not listed.

#### `llm_testing_results`
Contains results from testing the LLM model.

- `lora_plus_rag_testing_output.csv`: CSV file containing the output from testing the LORA + RAG QA generator.

#### `summaries`
Folder containing summary files for API references, with a sample of 3 files shown and a total of 830 files.

---

## Usage

For details on the data and how to use them in the project, refer to the individual YAML, CSV, JSON, and TXT files within each sub-directory.

**Note:** Due to the large number of files, only a subset is displayed for directories containing many files. Refer to the respective folders for the complete list of files.

## Contact

For any queries or issues, refer to the project documentation or contact the project maintainers.
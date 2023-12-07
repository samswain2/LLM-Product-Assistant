## Folder Structure
Below you will find the folder structure of this sub-directory:

```
├── 00_instructions.gitkeep
├── 01_lora_and_rag_answer_generator.py
├── 02_lora_and_rag_output_format.py
├── 00_trained_lora_model/
    ├── .gitkeep
```

### Instructions
To run the LORA + RAG QA generator:
1. **Model Acquisition**: Obtain the LORA model from a member of the Fall 2023 Amazon Capstone team, Northwestern's MLDS program. Place it in the `00_trained_lora_model` directory.
2. **Data Setup**: Ensure the testing file from `03_Data_Ingestion_Pipelines\VPC_Documentation_QA_Dataset_Generator` is accessible.
3. **Execution**: Run `01_lora_and_rag_answer_generator.py` followed by `02_lora_and_rag_output_format.py` in the given order.

### File Descriptions

#### `01_lora_and_rag_answer_generator.py`
This script initializes and utilizes a custom LLM chat model along with OpenAI embeddings and a Pinecone index manager. It processes a dataset of questions, retrieves relevant context using the Pinecone index, generates answers using the LLM model, and stores the results. Key steps include:
- Setting CUDA devices and initializing models.
- Reading and processing a CSV file containing question-answer pairs.
- Generating answers for each question based on retrieved context.
- Saving the generated answers in a new CSV file.

#### `02_lora_and_rag_output_format.py`
This script is designed to transform and clean a CSV file containing QA data. It performs various data manipulations such as:
- Renaming columns and converting them to lowercase.
- Removing unwanted columns.
- Extracting and cleaning the answer part of each entry.
- Saving the transformed data into a new CSV file.
- The script streamlines the output format to facilitate easier analysis and scoring of the QA pairs.
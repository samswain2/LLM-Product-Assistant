## Functions
This folder (and 08_Lora_and_Rag/ from the parent folder) contains what's needed to generate test results from the selected questions (48 Q&A pairs), and then to score these generated answers using selected metrics (BERTScore, BLUE, ROGUE).

## Directory structure 
```
# create test file for RAG and LoRa
├── testing/
    ├── RAG_test.py <- Python Script for testing RAG
    ├── lora_inference.ipynb <- Jupyter Notebook for testing QLoRa
    ├── test.csv <- Demo test dataset

# create test file for RAG + LoRa
├── ../08_Lora_and_Rag
    ├── 01_lora_and_rag_answer_generator.py <- create the test file
    ├── 02_lora_and_rag_output_format.py <- format the test file
    ├── test.py
    ├── 00_trained_lora_model/
        ├── .gitkeep

# scoring for all three
├── scoring/
    ├── score.ipynb
    ├── requirements.txt
    ├── data/ <- test output for different model approaches and scores
        ├── rag_output_test.csv <- RAG
        ├── llm_output_test.csv <- LoRa
        ├── rag_and_llm_output_test.csv <- RAG + LoRa
        ├── score_by_answer.csv <- score for all at the level of individual Q&A pair
        ├── score_by_model.csv <- score for all at the level of modeling approach
        ├── samples.csv <- Q&A pairs for demo
        
```

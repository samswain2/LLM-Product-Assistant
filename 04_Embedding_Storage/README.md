# Document Embedding and Uploading Script

## Overview
The `01_embed.py` script is designed to process a collection of text documents by generating embeddings using the OpenAI API, and uploading these embeddings to a Pinecone index. The index enables efficient similarity searching and retrieval, facilitating the development of applications that require semantic understanding of text data.

```
├── 01_embed.py
├── README.md
```

## Key Components

- `EmbeddingManager`: Manages the embedding generation with OpenAI and operations within Pinecone.
- `DocumentProcessor`: Handles reading of documents and associated metadata, preparing them for the embedding process.
- `generate_and_upload_embeddings`: Orchestrates the generation of embeddings for documents and uploads them to the Pinecone index.

## Usage

Before running the script, ensure that all required libraries are installed and that the `.env` file is correctly configured with the necessary API keys.

Set the variables `links_csv_path` and `folder_path` to the respective paths of your documents.

Execute the script to process documents, generate embeddings, and upload them to the Pinecone index.

## Requirements

- An OpenAI API key and a Pinecone API key are required. These should be placed in an `.env` file.
- Ensure error handling and logging are set up for a robust operation.

## Contact

For any queries or issues, refer to the project documentation or contact the project maintainers.
import os
import csv
import openai
from dotenv import load_dotenv
import pinecone

# Load environment variables
load_dotenv()
pinecone_key = os.getenv("PINECONE_KEY")
openai.api_key = os.getenv("OPENAI_KEY")

# Function to get embeddings
def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)['data'][0]['embedding']

# Read and parse the CSV file for links
links_csv_path = "06_Data/Capstone_Data/VPC Links List - Sheet1.csv"
link_mapping = {}
with open(links_csv_path, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header
    for row in csvreader:
        link_mapping[row[0]] = row[1]

# Print the first few entries in the link mapping for debugging
print("First few entries in link mapping:")
for key in list(link_mapping.keys())[:5]:
    print(f"{key}: {link_mapping[key]}")

# Adjusted folder path to include subfolder
folder_path = "06_Data/Capstone_Data/chunks/"
document_metadata = []

# Modify the file reading loop with the updated prefix extraction logic
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith('.txt'):
            with open(os.path.join(root, filename), 'r', encoding='utf-8') as f:
                content = f.read()
                prefix = filename.rpartition('_')[0]  # Extract prefix
                link = link_mapping.get(prefix, "No link found")
                full_text = "SOURCE LINK: " + link + " " + "CONTENT: " + content
                document_metadata.append((full_text, link))

# Test with a small subset of documents (e.g., first 10)
test_documents = document_metadata[:10]

# Verify that documents are being read
print(f"Number of documents read: {len(test_documents)}")

# Initialize Pinecone
pinecone.init(api_key=pinecone_key, environment='gcp-starter')

# Set index name
index_name = "document-embeddings"

# Determine the dimension of the embeddings
test_embedding_dim = len(get_embedding("Test text to determine embedding dimension"))

# Check if the index exists, and create it if it doesn't
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=test_embedding_dim)

index = pinecone.Index(index_name)

# Get embeddings for the test documents and prepare metadata
embeddings = [get_embedding(doc[0]) for doc in test_documents]
vectors = []
for i, embedding in enumerate(embeddings):
    text, link = test_documents[i]
    vector = {
        'id': str(i),
        'values': [float(value) for value in embedding],
        'metadata': {'text': text, 'link': link}
    }
    vectors.append(vector)

# Upload embeddings to Pinecone
index.upsert(vectors=vectors)

print(f"Number of vectors uploaded: {len(vectors)}")

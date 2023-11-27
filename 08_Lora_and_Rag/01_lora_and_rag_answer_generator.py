import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel
import openai
import pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

# Custom LLM Setup
base_model_id = "NousResearch/Llama-2-7b-hf"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)
base_model = AutoModelForCausalLM.from_pretrained(
    base_model_id, 
    quantization_config=bnb_config, 
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(base_model_id, add_bos_token=True, trust_remote_code=True)
path_llm_model = "08_Lora_and_Rag/00_trained_lora_model/lora_finetuning/llama2-7b-AmazonVPC-finetune/checkpoint-500"
ft_model = PeftModel.from_pretrained(base_model, path_llm_model)

# Custom LLM Chat Model Class
class CustomLLMChatModel:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer

    def _call(self, prompt, stop_words=None):  # Implementing the required _call method
        model_input = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        self.model.eval()
        with torch.no_grad():
            output = self.model.generate(**model_input, max_new_tokens=500)[0]
            raw_output = self.tokenizer.decode(output, skip_special_tokens=True)
            return raw_output

    @property
    def _identifying_params(self):  # Optional _identifying_params property
        return {"model": str(self.model), "tokenizer": str(self.tokenizer)}

# Load environment variables
load_dotenv()
pinecone_key = os.getenv("PINECONE_KEY")
openai.api_key = os.getenv("OPENAI_KEY")
index_name = "document-embeddings"
environment = "gcp-starter"

# Initialize Pinecone
pinecone.init(api_key=pinecone_key, environment=environment)
index = pinecone.Index(index_name)

# Langchain Setup
vector_db = Pinecone.from_existing_index(index_name=index_name, embedding=OpenAIEmbeddings(openai_api_key=openai.api_key))
vector_db_retriever = vector_db.as_retriever()
ans_template = """
    Context: The following API reference information has been retrieved based on the user's question. Pay attention to function names, parameters, and any mentioned errors. Use this information to provide a technically accurate answer.

    Retrieved API Information: {context}
    
    Question: {question}
    
    Answer:
"""
prompt_for_chain = PromptTemplate(template=ans_template, input_variables=["context", "question"])
custom_llm_model = CustomLLMChatModel(ft_model, tokenizer)
assistant = RetrievalQA.from_chain_type(llm=custom_llm_model,
                                        retriever=vector_db_retriever,
                                        chain_type="stuff",
                                        chain_type_kwargs={"prompt": prompt_for_chain})

# Read CSV File
test_df = pd.read_csv('06_Data/Capstone_Data/documentation_qa_datasets/Final_FILTERED_TEST_Question_Answer_Pairs.csv')

# # Process and Generate Answers
# for index, row in test_df.iterrows():
#     llm_answer = assistant.run(row['Question'])
#     test_df.loc[index, 'llm_answer'] = llm_answer

# Select a subset of the data for testing, e.g., 10%
subset_percentage = 0.1
test_subset = test_df.sample(frac=subset_percentage)

# Process and Generate Answers for the subset
for index, row in test_subset.iterrows():
    llm_answer = assistant.run(row['Question'])
    test_df.loc[index, 'llm_answer'] = llm_answer  # Store the answer back in the original DataFrame

# Save Results to New CSV
test_df.to_csv('/06_Data/Capstone_Data/llm_testing_results/lora_plus_rag_testing_output.csv', index=False)

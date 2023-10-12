import openai
import pinecone
from dotenv import load_dotenv
import os

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI


### TESTING

import tkinter as tk
from tkinter import ttk, scrolledtext

### TESTING


# Load variables
load_dotenv()
pinecone_key = os.getenv("PINECONE_KEY")
openai.api_key = os.getenv("OPENAI_KEY")
index_name = "document-embeddings"
environment = "gcp-starter"
model_name = "gpt-3.5-turbo-16k"
ans_template = """
    Use the following pieces of context to answer the question at the end.
    Pay attention to the tone of the question and use it to determine the 
    technical familiarity of the user with the product, and then adjust your 
    answer accordingly. If you do not know the answer, advise the user to 
    seek help via king wencheng support. {context} 
    
    Question: {question} Answer tailored to the technical familiarity of 
    the user:
    """


# Initialize pinecone session
pinecone.init(api_key=pinecone_key, environment=environment)
index = pinecone.Index(index_name)


# Set up langchain pipeline
vector_db = Pinecone.from_existing_index(index_name=index_name, embedding=OpenAIEmbeddings(openai_api_key=openai.api_key))
vector_db_retriever = vector_db.as_retriever()
prompt_for_chain = PromptTemplate(template = ans_template, input_variables = ["context", "question"])
llm = ChatOpenAI(temperature=0, model_name=model_name, openai_api_key=openai.api_key)
assistant = RetrievalQA.from_chain_type(llm = llm,
                                        retriever = vector_db_retriever,
                                        chain_type = "stuff",
                                        chain_type_kwargs = {"prompt": prompt_for_chain})


### TESTING

# Function Definitions
def get_assistant_response(user_query):
    """
    Query the chatbot assistant and get a response.

    Parameters:
    - user_query (str): The query to pass to the assistant.

    Returns:
    str: The assistant's response to the query.
    """
    return assistant.run(user_query)

def append_to_chat_history(message):
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, message + "\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)

def submit_query():
    user_query = user_input.get()
    append_to_chat_history("You: " + user_query)
    response = get_assistant_response(user_query)
    append_to_chat_history("Assistant: " + response)
    user_input.delete(0, tk.END)


# Tkinter setup
root = tk.Tk()
root.title("ChatGPT Assistant")
root.geometry("400x500")  # Set a default window size

frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Create a scrolled text widget for chat history
chat_history = scrolledtext.ScrolledText(frame, wrap=tk.WORD, height=15, font=("Arial", 12))
chat_history.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
chat_history.config(state=tk.DISABLED)  # By default, the chat history is not editable

user_input = ttk.Entry(frame, width=40, font=("Arial", 12))
user_input.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)

submit_button = tk.Button(frame, text="Submit", command=submit_query, font=("Arial", 12))
submit_button.grid(row=1, column=1, sticky=tk.W, padx=5)

root.mainloop()

### TESTING
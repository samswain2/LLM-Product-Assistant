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

from flask import Flask, render_template, request, jsonify

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

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_query = request.get_json().get('query')
        response = get_assistant_response(user_query)
        return jsonify(response=response)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

### TESTING
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
import os 

#Load the token 
HF_TOKEN = os.environ.get("HF_TOKEN")

huggingface_repoid = "mistralai/Mistral-7B-Instruct-v0.3"

def load_llm(huggingface_repoid):
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repoid,

        model_kwargs={
            "token":HF_TOKEN
            "temperature": 0.5,
            "max_new_tokens": 500,
            
        }
    )
    return llm 



    
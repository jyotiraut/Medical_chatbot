from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATA_PATH ="data/"

def load_data_files(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    print("Workin")
    documents = loader.load()
    return documents


documents = load_data_files(data=DATA_PATH)
print("Length of data is ",len(documents))

#create chunks 
def create_chunks(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(extracted_data)
    return chunks

text_chunks = create_chunks(documents)
print("Length of chunks",len(text_chunks))

#embeddings 
def get_embedding_model():
    embedding_model=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model=get_embedding_model()


embedding_model =  get_embedding_model(embedding_model)


 #store embedding in FAISS
DB_FAISS_PATH = "vectorstore/db_faiss"
db = FAISS.from_document(text_chunks,embedding_model)
db.save_local(DB_FAISS_PATH)




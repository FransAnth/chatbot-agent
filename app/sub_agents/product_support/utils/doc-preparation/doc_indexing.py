from chromadb import PersistentClient
from chromadb.config import Settings
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings

load_dotenv()

file_path = r"app\sub_agents\product_support\utils\output-files\billease_faq.txt"
persist_directory = r"app\vectorstore"

CHROMA_SETTINGS = Settings(
    persist_directory=persist_directory,
    chroma_db_impl="duckdb+parquet",
    anonymized_telemetry=False,
)
collection_name = "billease_vectorstore"
embeddings = OpenAIEmbeddings()

client = PersistentClient(path=persist_directory)
db = Chroma(
    persist_directory=persist_directory,
    embedding_function=embeddings,
    client=client,
)


text_loader = TextLoader(file_path)
file = text_loader.load()


text_splitter = CharacterTextSplitter(separator="---", chunk_size=500, chunk_overlap=0)
doc_chunks = text_splitter.split_documents(file)

vectordb = Chroma(
    collection_name=collection_name,
    embedding_function=embeddings,
    persist_directory=persist_directory,
)

print("LENght", len(doc_chunks))

vectordb.add_documents(doc_chunks)

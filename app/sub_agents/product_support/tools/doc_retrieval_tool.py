from agents import function_tool
from chromadb import PersistentClient
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

persist_directory = r"app\vectorstore"
collection_name = "billease_vectorstore"
embeddings = OpenAIEmbeddings()


@function_tool
def retrieve_relevant_doc(query: str):
    """
    Retrieves information that are relevant in answering the query question

    Args:
        query (str): The query or question that will be used to make a similarity search and retrieve relevant information
    """
    print("Doc retrieval tool running...")
    print("Query:", query)

    vectorstore = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=persist_directory,
    )

    results = vectorstore.similarity_search(query, k=1)
    if len(results) == 0:
        print("No relevant information retrieved")
        return "No relevant information retrieved"
    information = "\n".join([result.page_content for result in results])

    print("Retrieved Knowledge")
    print(information)
    return information

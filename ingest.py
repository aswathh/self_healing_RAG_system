import os
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import chromadb

# initialise ChromaDB

load_dotenv()

Chroma_client = chromadb.PersistentClient(path="./chromadb")
collections = Chroma_client.get_or_create_collection(
    name="Knowledge_base",
    metadata={"hnsw:space":"cosine"},
)

#load and split chunks

def load_and_split(docs_folder: str):
    """load the .txt file from the folder and split it"""
    Total_chunks=[]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
    )
    doc_folder = Path(docs_folder)
    for txt_file in doc_folder.glob("*.txt"):
        loader=TextLoader(str(txt_file), encoding="utf-8")
        documents=loader.load()
        chunks=text_splitter.split_documents(documents)
        Total_chunks.extend(chunks)
        print(f"loaded {len(chunks)} chunks from {txt_file.name}")

    return Total_chunks
    
# store the chunks in chromadb

def ingest_to_chromadb(chunks: list):
    """store the chunks in chromadb"""
    documents = [chunk.page_content for chunk in chunks]
    ids = [f"chunk_{i}"for i in range(len(chunks))]
    metadatas=[
        {"source": chunk.metadata.get("source", "unknown")}
        for chunk in chunks
        ]

    collections.add(
            documents=documents,
            ids=ids,
            metadatas=metadatas
        )

    print(f"stored {len(chunks)} in chromaDB")

# The main runner

if __name__ == "__main__":
    print("starting document ingestion")
    chunks=load_and_split("docs")

    if not chunks:
        print("No .txt_files found in the docs/folder")
        
    else:
        ingest_to_chromadb(chunks)
        print(f"Done! Total chunks stored:{len(chunks)}")
        print("your knowledge base is ready")





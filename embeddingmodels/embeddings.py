from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(
    model='text-embedding-3-small',
    dimensions=64
    
)
texts=["Hello world",
        "How are you?", 
        "This is a test of the embedding model."]

vector=embeddings.embed_documents(texts)

print(vector)
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9, max_tokens=100)


response = model.invoke("Write a poem on Virat kohli")

print(response.content)
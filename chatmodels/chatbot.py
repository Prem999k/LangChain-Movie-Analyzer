from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (AIMessage,HumanMessage,SystemMessage)

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",temperature=0.9,max_tokens=100)

modes = {
    "1": "You are a Funny AI Agent.",
    "2": "You are an Angry AI Agent.",
    "3": "You are a Sad AI Agent."
}

current_mode = "1"

chatMessages = [
    SystemMessage(content=modes[current_mode])
]

print("\n----------- CHAT BOT -----------")
print("1 = Funny 😂")
print("2 = Angry 😡")
print("3 = Sad 😢")
print("0 = Exit\n")

while True:

    prompt = input("You: ")

    if prompt == "0":
        print("Exiting Chat...")
        break

    if prompt in modes:

        current_mode = prompt

        chatMessages = [
            SystemMessage(content=modes[current_mode])
        ]

        print(f"Switched to Mode {current_mode}")

        continue

    chatMessages.append(HumanMessage(content=prompt))

    response = model.invoke(chatMessages)

    chatMessages.append(AIMessage(content=response.content))

    print("Bot:", response.content)
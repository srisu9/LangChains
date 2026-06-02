from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')

]

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.7
    )
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('Ai: ',result.content)
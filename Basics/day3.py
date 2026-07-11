from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a professional Python teacher."),
        MessagesPlaceholder(variable_name="history", optional=True),
        ("human", "{question}")
    ]
)

parser = StrOutputParser()
chain = prompt | model | parser
history = [
    HumanMessage(content="What is Python?"),
    AIMessage(content="Python is a programming language."),
    HumanMessage(content="What is a variable?"),
    AIMessage(content="A variable is used to store data.")
]
formatted_prompt = prompt.invoke(
    {
        "history": history,
        "question": "Who created Python?"
    }
)

print("=" * 60)
print("PROMPT SENT TO THE MODEL")
print("=" * 60)

for message in formatted_prompt.messages:
    print(f"\nType : {type(message).__name__}")
    print(f"Content : {message.content}")

print("\n" + "=" * 60)
print("MODEL RESPONSE")
print("=" * 60)

response = chain.invoke(
    {
        "history": history,
        "question": "Who created Python?"
    }
)

print(response)
response1 = chain.batch(
    [
    
        {"question": "who is the owner of python"},
        {"question": "What is c++"},
        {"question": "when python was released and in which country"}
    ]
)
for i, answer in enumerate(response1, start=1):
    print(f"\nAnswer {i}:")
    print(answer)
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

message = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a professional Python teacher."),
        ("human", "{question}")
    ]
)

parser = StrOutputParser()
chain = message | model | parser

for chunk in chain.stream(
    {
        "question":"Explain python loops"
    }

):
    print(chunk, end="", flush=True)

response1 = chain.batch(
    [
        {"question": "Explain functions."},
        {"question": "Explain DSA in Python."},
        {"question": "Explain decorators in Python."}
    ]
)

for i, answer in enumerate(response1, start=1):
    print(f"\nAnswer {i}:")
    print(answer)
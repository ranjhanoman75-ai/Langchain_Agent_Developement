print("==========Day 6=======RunnableLamda=============")
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGroq(model = "llama-3.3-70b-versatile")
parser = StrOutputParser()

def uppercase(text:str):
    return text.upper()
uppercase_runnable = RunnableLambda(uppercase)
chain = uppercase_runnable | model | parser
response  = uppercase_runnable.invoke(
    "Explain the python loops"
)   
print(response)


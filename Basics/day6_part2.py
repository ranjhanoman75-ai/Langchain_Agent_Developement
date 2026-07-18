print("===============Day 6=======RunnablePassThrough=========")
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

model  = ChatGroq(model="llama-3.3-70b-versatile")
parser  = StrOutputParser()
passthrough = RunnablePassthrough()
chain = passthrough | model | parser
response = chain.invoke(
    "explain the python loops"
)
print(response)
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model = "llama-3.3-70b-versatile")
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} like i am 10 years old."
)
parser = StrOutputParser()
chain = prompt | model | parser
response = chain.invoke(
    {"topic": "Python"}
)
print(response)


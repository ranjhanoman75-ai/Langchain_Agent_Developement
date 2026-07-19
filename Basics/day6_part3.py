from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableParallel,RunnablePassthrough,RunnableLambda

def uppercase(text:str):
    return text.upper()
def length(text:str):
    return len(text)
length_runnable = RunnableLambda(length)
uppercase_runnable = RunnableLambda(uppercase)
parallel = RunnableParallel(
    original = RunnablePassthrough(),
    uppercase = uppercase_runnable,
    length  = length_runnable
)
response = parallel.invoke(
    "python"
)
print(response)
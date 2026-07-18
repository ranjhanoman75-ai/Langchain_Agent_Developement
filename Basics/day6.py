print("==========Day 6=======RunnableLamda=============")
from langchain_core.runnables import RunnableLambda
def square(numbers):
    return numbers * numbers

square_runnable = RunnableLambda(square)
print(square_runnable.invoke(10))

def uppercase(text:str):
    return text.upper()
uppercase_runnable = RunnableLambda(uppercase)
print(uppercase_runnable.invoke("Python"))
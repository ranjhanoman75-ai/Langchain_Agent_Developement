print("==========Day 6=======RunnableLamda=============")
from langchain_core.runnables import RunnableLambda
def square(numbers):
    return numbers * numbers

square_runnable = RunnableLambda(square)
print(square_runnable.invoke(10))
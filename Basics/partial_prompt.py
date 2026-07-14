from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
prompt = PromptTemplate(
    template="""
You are a {role}.

Explain the topic in {language}.

Question:
{question}
""",
    input_variables=["question"],
    partial_variables={
        "role": "Professional Python Teacher",
        "language": "simple English"
    }
)

parser = StrOutputParser()
chain = prompt | model | parser
formatted_prompt = prompt.invoke(
    {
        "question": "Explain Python loops."
    }
)

print("=" * 60)
print("FORMATTED PROMPT")
print("=" * 60)
print(formatted_prompt)
print("\n" + "=" * 60)
print("SINGLE RESPONSE")
print("=" * 60)

response = chain.invoke(
    {
        "question": "Explain Python loops."
    }
)

print(response)

questions = [
    {"question": "Explain Python functions."},
    {"question": "Explain Python classes."},
    {"question": "Explain Python decorators."}
]

responses = chain.batch(questions)

print("\n" + "=" * 60)
print("BATCH RESPONSES")
print("=" * 60)

for i, answer in enumerate(responses, start=1):
    print(f"\nAnswer {i}")
    print("-" * 40)
    print(answer)
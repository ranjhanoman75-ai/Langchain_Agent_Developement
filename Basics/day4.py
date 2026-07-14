print("============== Day 4 Output Parsers ==============")

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

parser = JsonOutputParser()

format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional Python teacher.

Always return ONLY valid JSON.

Do not include markdown.
Do not include explanations.
Do not include extra text.

{format_instructions}
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)


chain = prompt | model | parser

response = chain.invoke(
    {
        "question": "Explain the Python decorators.",
        "format_instructions": format_instructions
    }
)

print(response)
print(type(response))


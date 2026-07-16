print("===========Pydantic Output parser===============")
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import Field, BaseModel

load_dotenv()
model = ChatGroq(model = "llama-3.3-70b-versatile")
class PythonTopic(BaseModel):
    topic :str = Field(
        description="Name of the topic"
    )
    description : str =Field(
        description="Detailed Description..."
    )
    example:str = Field(
        description="Example of Topic .."
    )

parser  = PydanticOutputParser(
    pydantic_object=PythonTopic
)
prompt  = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are professional python teacher.
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
        "question": "Explain the pytho loops .",
        "format_instructions": parser.get_format_instructions()
    }
)
print(response)
print(type(response))
print(response.topic)
print(response.description)
print(response.example)
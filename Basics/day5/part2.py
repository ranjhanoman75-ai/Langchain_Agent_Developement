print("================structured output==============")
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import Field,BaseModel

load_dotenv()
model  = ChatGroq(model="llama-3.3-70b-versatile")
class Pythontopic(BaseModel):
    topic:str = Field(
        description="Name of the topic"
    )
    description:str = Field(
        description="Detailed explaination"
    )
    example:str = Field(
        description= "Example "
    )
structured_model = model.with_structured_output(Pythontopic)
response = structured_model.invoke(
    "Explain python decorators."
)
print(response)
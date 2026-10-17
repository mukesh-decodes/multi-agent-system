from pydantic import BaseModel, Field

class Answer(BaseModel):
    ans:str= Field(description="String of tokens from model in response to query",)
    topic:list[str] =Field(description="Main topics covered in response")
    confidence:float =Field(description="Confidence the model has on ans",)

class AnswerWithTools(BaseModel):
    ans:str=Field(description="String of tokens from model in repsonse")
    topic: list[str] =Field(description="main topics covered")
    tools: list[str] = Field(description="Names of tools used")
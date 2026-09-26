from pydantic import BaseModel, Field

class Answer(BaseModel):
    ans:str= Field(description="String of tokens from model in response to query",)
    topic:list[str] =Field(description="Main topics covered in response")
    confidence:float =Field(description="Confidence the model has on ans",)


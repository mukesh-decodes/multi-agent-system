from langchain_core.prompts import ChatPromptTemplate

prompt_template_for_country = ChatPromptTemplate.from_template(
    "Why is {country} so {state} in less than 20 words ?"
)